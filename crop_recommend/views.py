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
            nitrogen = request.POST.get('nitrogen', '').strip()
            phosphorus = request.POST.get('phosphorous', '').strip()
            potassium = request.POST.get('potassium', '').strip()
            phlevel = request.POST.get('phlevel', '').strip()
            temperature = request.POST.get('temperature', '').strip()
            humidity = request.POST.get('humidity', '').strip()
            rainfall = request.POST.get('rainfall', '').strip()

            # Convert to float and use default values if needed
            nitrogen = float(nitrogen) if nitrogen else defaults['nitrogen']
            phosphorus = float(phosphorus) if phosphorus else defaults['phosphorous']
            potassium = float(potassium) if potassium else defaults['potassium']
            phlevel = float(phlevel) if phlevel else defaults['phlevel']
            temperature = float(temperature) if temperature else defaults['temperature']
            humidity = float(humidity) if humidity else defaults['humidity']
            rainfall = float(rainfall) if rainfall else defaults['rainfall']

            # Path to the model file (relative path)
            model_path = os.path.join(os.path.dirname(__file__), 'crop_recommend.pkl')
            
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
