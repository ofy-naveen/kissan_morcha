import pickle
import numpy as np
import xgboost

# Load the model
with open('crop_recommend.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the input features (example values provided)
nitrogen = 90
phosphorus = 40
potassium = 40
phlevel = 6.5
temperature = 22.0
rainfall = 150.0
humidity = 80.0

# Combine features into a numpy array
features = np.array([[nitrogen, phosphorus, potassium, phlevel, temperature, rainfall, humidity]])

# Make a prediction
predicted_crop = model.predict(features)

print(f"The recommended crop is: {predicted_crop[0]}")
