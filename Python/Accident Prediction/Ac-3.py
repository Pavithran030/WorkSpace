import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import smtplib
from email.mime.text import MIMEText
import datetime
import time

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
    password = "Hacker@780"

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

# Predict future hotspots
def predict_hotspot(current_data):
    prediction = model.predict(current_data)
    return prediction[0]

# Simulate real-time data collection with proper feature names
""" def collect_data():
    current_data = [
        datetime.datetime.now().hour,  # Current hour
        datetime.datetime.now().weekday(),  # Day of the week
        np.random.randint(50, 200),  # Simulated traffic density
        np.random.randint(0, 5)  # Simulated accident history
    ]
    # Return data as pandas DataFrame for compatibility with model
    return pd.DataFrame([current_data], columns=["time", "day_of_week", "traffic_density", "accident_history"])
"""

def collect_data():
    # Simulated data collection
    current_data = [
        datetime.datetime.now().hour,  # Current hour (Time)
        datetime.datetime.now().weekday(),  # Day of the week (DayOfWeek)
        np.random.randint(50, 200),  # Simulated traffic density (TrafficDensity)
        np.random.randint(0, 5)  # Simulated accident history (AccidentHistory)
    ]
    
    # Return the data with the correct feature names (matching those used during training)
    return pd.DataFrame([current_data], columns=["Time", "DayOfWeek", "TrafficDensity", "AccidentHistory"])

if __name__ == "__main__":
    # Predict and send alert
    print("Starting accident hotspot prediction...")
    while True:
        current_data = collect_data()
        prediction = predict_hotspot(current_data)

        if prediction == 1:  # 1 indicates a high-risk hotspot
            send_alert("Traffic Signal - Main Road")

        # Simulate a delay for real-time processing
        time.sleep(10)
