import cv2
import math
import numpy as np
from ultralytics import YOLO
import config
from alert_system import trigger_alert

model = YOLO(config.MODEL_NAME)

prev_gray = None

# dangerous objects list
danger_objects = ["knife","scissors","baseball bat","bottle"]

def run_detection():

    global prev_gray

    cap = cv2.VideoCapture(config.CAMERA_ID)

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        people_boxes = []
        object_count = 0
        danger_detected = False

        for r in results:
            for box in r.boxes:

                cls = int(box.cls[0])
                label = model.names[cls]
                conf = float(box.conf[0])

                x1,y1,x2,y2 = map(int,box.xyxy[0])

                color = (0,255,0)

                # highlight dangerous objects
                if label in danger_objects:
                    color = (0,0,255)
                    danger_detected = True

                # draw box
                cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)

                text = f"{label} {conf:.2f}"

                cv2.putText(frame,text,
                            (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,color,2)

                object_count += 1

                # store people for violence detection
                if label == "person":
                    people_boxes.append((x1,y1,x2,y2))

        people_count = len(people_boxes)

        cv2.putText(frame,f"People: {people_count}",
                    (20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        cv2.putText(frame,f"Objects: {object_count}",
                    (20,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        motion_score = 0

        if prev_gray is not None:
            diff = cv2.absdiff(prev_gray,gray)
            motion_score = np.sum(diff)/1000000

        prev_gray = gray

        violence = False
        threat = "LOW"

        if people_count >= 2:

            for i in range(len(people_boxes)):
                for j in range(i+1,len(people_boxes)):

                    x1,y1,x2,y2 = people_boxes[i]
                    x3,y3,x4,y4 = people_boxes[j]

                    cx1 = (x1+x2)//2
                    cy1 = (y1+y2)//2

                    cx2 = (x3+x4)//2
                    cy2 = (y3+y4)//2

                    distance = math.sqrt((cx1-cx2)**2 + (cy1-cy2)**2)

                    if distance < config.DISTANCE_THRESHOLD and motion_score > config.MOTION_THRESHOLD:
                        violence = True
                        threat = "HIGH"

                    elif distance < config.DISTANCE_THRESHOLD:
                        threat = "MEDIUM"

        cv2.putText(frame,f"Threat Level: {threat}",
                    (20,120),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

        if danger_detected:

            cv2.putText(frame,"⚠ DANGEROUS OBJECT DETECTED",
                        (20,160),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

            trigger_alert(frame, config.ALERT_COOLDOWN)

        if violence:

            cv2.putText(frame,"⚠ VIOLENCE DETECTED",
                        (20,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

            trigger_alert(frame, config.ALERT_COOLDOWN)

        cv2.imshow("AI CCTV Violence Detection System",frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()