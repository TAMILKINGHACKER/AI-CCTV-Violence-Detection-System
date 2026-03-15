from detection import run_detection
from utils import ensure_folders

def main():
    ensure_folders()
    print("Starting AI CCTV Violence Detection System...")
    run_detection()

if __name__ == "__main__":
    main()
