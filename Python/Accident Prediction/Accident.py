import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import smtplib
from email.mime.text import MIMEText
import datetime

# Load pre-trained model for prediction
MODEL_PATH = "hotspot_predictor_model.pkl"
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print("Pre-trained model not found! Train the model first.")
    exit()

# Email alert function
def send_alert(location):
    sender_email = "godofhacker780@gmail.com"
    receiver_email = "learncoding676@gmail.com"
    password = "hacker@780"

    subject = "Accident Hotspot Alert"
    body = f"Alert: High risk of accidents detected at {location} on {datetime.datetime.now()}! Immediate action required."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Alert sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Real-time vehicle and person motion detection
def detect_motion_and_activity(video_source):
    cap = cv2.VideoCapture(video_source)
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply background subtraction
        fgmask = fgbg.apply(blur)
        _, thresh = cv2.threshold(fgmask, 127, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filter small movements
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Frame", frame)

        # Use key press to break
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Predict future hotspots
def predict_hotspot(current_data):
    prediction = model.predict([current_data])
    return prediction[0]

# Simulate real-time data collection
def collect_data():
    # Example data: [time, day_of_week, traffic_density, accident_history]
    current_data = [datetime.datetime.now().hour, datetime.datetime.now().weekday(), np.random.randint(50, 200), np.random.randint(0, 5)]
    return current_data

if __name__ == "__main__":
    video_source = 0  # Use the first webcam as the video source

    # Start motion and activity detection in a separate thread
    print("Starting motion and activity detection...")
    detect_motion_and_activity(video_source)

    # Predict and send alert
    while True:
        current_data = collect_data()
        prediction = predict_hotspot(current_data)

        if prediction == 1:  # 1 indicates a high-risk hotspot
            send_alert("Traffic Signal - Main Road")

        # Simulate a delay for real-time processing
        time.sleep(10)
