import winsound
import cv2
import time
import requests
import config
from utils import log_event, ensure_folders

last_alert = 0


def send_telegram_alert(image_path):

    url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendPhoto"

    files = {
        "photo": open(image_path, "rb")
    }

    data = {
        "chat_id": config.CHAT_ID,
        "caption": "⚠ Violence Detected!"
    }

    response = requests.post(url, files=files, data=data)

    print("Telegram response:", response.text)


def trigger_alert(frame, cooldown):

    global last_alert

    if time.time() - last_alert > cooldown:

        ensure_folders()

        filename = f"evidence/violence_{int(time.time())}.jpg"

        cv2.imwrite(filename, frame)

        # Alarm sound
        winsound.Beep(1000, 500)

        # Send Telegram alert
        send_telegram_alert(filename)

        log_event("Violence detected")

        print("ALERT: Violence detected")
        print("Evidence saved:", filename)

        last_alert = time.time()