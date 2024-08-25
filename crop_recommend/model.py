from django.shortcuts import render
import pickle
import numpy as np
import os

def crop_recommend(request):
    # Default values
    defaults = {
        'nitrogen': 45,
        'phosphorous': 4,
        'potassium': 4,
        'phlevel': 9,
        'temperature': 22.0,
        'rainfall': 150.0,
        'humidity': 80.0
    }
    
    predicted_crop = None
    error_message = None

    if request.method == 'POST':
        try:
            # Extracting form data with defaults
            nitrogen = float(request.POST.get('nitrogen', defaults['nitrogen']))
            phosphorus = float(request.POST.get('phosphorous', defaults['phosphorous']))
            potassium = float(request.POST.get('potassium', defaults['potassium']))
            phlevel = float(request.POST.get('phlevel', defaults['phlevel']))
            temperature = float(request.POST.get('temperature', defaults['temperature']))
            humidity = float(request.POST.get('humidity', defaults['humidity']))
            rainfall = float(request.POST.get('rainfall', defaults['rainfall']))

            # Path to the model file
            model_path = '/crop_recommend.pkl'
            
            # Check if the model file exists
            if not os.path.exists(model_path):
                raise FileNotFoundError("Model file not found. Please ensure the path is correct.")

            # Load the model
            with open(model_path, 'rb') as model_file:
                model = pickle.load(model_file)

            # Combine features into a numpy array
            features = np.array([[nitrogen, phosphorus, potassium, phlevel, temperature, rainfall, humidity]])

            # Make a prediction
            predicted_crop = model.predict(features)[0]

        except (ValueError, TypeError) as e:
            error_message = f"Error processing input data: {e}"
        except FileNotFoundError as e:
            error_message = str(e)
        except pickle.UnpicklingError:
            error_message = "Error unpickling the model. The file may be corrupted."
        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"

    return render(request, "cropRecommender.html", {
        'predicted_crop': predicted_crop,
        'error_message': error_message
    })
