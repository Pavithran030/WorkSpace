import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Paths for dataset and model
DATA_PATH = "traffic_dataset.csv"
MODEL_PATH = "hotspot_predictor_model.pkl"

def train_model(data_path, model_path):
    try:
        # Load dataset
        data = pd.read_csv(data_path)
        
        # Print column names for verification
        print("Dataset Columns:", data.columns.tolist())
        
        # Ensure necessary columns are present
        required_columns = ["Time", "DayOfWeek", "TrafficDensity", "AccidentHistory", "IsHotspot"]
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Dataset must contain columns: {required_columns}")

        # Features and target
        X = data[["Time", "DayOfWeek", "TrafficDensity", "AccidentHistory"]]
        y = data["IsHotspot"]

        # Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model accuracy: {accuracy * 100:.2f}%")

        # Save the model
        joblib.dump(model, model_path)
        print(f"Model saved as '{model_path}'.")

    except Exception as e:
        print(f"Error training model: {e}")

# Train the model using the provided dataset
if __name__ == "__main__":
    train_model(DATA_PATH, MODEL_PATH)
