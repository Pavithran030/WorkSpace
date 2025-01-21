import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

url="D:\\Whatsapp\\Maths\\weather_prediction_dataset.csv" # accessing the content of the CSV file on GitHub
dataset = pd.read_csv(url)
label = set(dataset['Rain'])
dataset['Rain'] = dataset['Rain'].map({'No':0,'Yes':1}).astype(int)
X = dataset.drop('Rain',axis='columns')
Y = dataset.Rain

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=0)

model = GaussianNB()
model.fit(X_train,Y_train)
Y_predict = model.predict(X_test)


print(f"Accuracy of the predictive model : {accuracy_score(Y_test,Y_predict)*100} % ")

try :
  temperature = float(input("Enter the temperature:"))
  humidity = float(input("Enter the humidity :"))
  windspeed = float(input("Enter the Wind Speed (km/h) :"))
  precipitation = float(input("Enter the Precipitation (mm) :"))
  cloudcover = float(input("Enter the Cloud Cover (%) :"))

  features = ['Temperature (°C)','Humidity (%)','Wind Speed (km/h)','Precipitation (mm)','Cloud Cover (%)']
  input_data = [[temperature,humidity,windspeed,precipitation,cloudcover]]

  currentdata = pd.DataFrame(input_data,columns=features)
  result = model.predict(currentdata)

  if result == 1:
    print("\nBased on the current weather conditions, there is a high chance of rain.\nIt would be wise to carry an umbrella or wear a raincoat if you plan to go outside.")
  else:
    print("\nBased on the current weather conditions, there is a low chance of rain.\nYou can enjoy your outdoor activities without worrying too much about getting wet.")

except :
  print("Invalid input, please try again.")