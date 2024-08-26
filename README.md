# Farmeasy Crop Recommendation System

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Farmeasy is a web application designed to assist farmers by recommending the best crops to grow based on soil properties, location, and weather data. This system aims to optimize crop yield by leveraging machine learning models and real-time data.

## Features
- *Crop Recommendation:* Predict the most suitable crop based on soil properties, temperature, humidity, and rainfall.
- *Location-based Soil Properties:* Automatically fill soil properties based on the user's location.
- *Weather Data Integration:* Fetch current weather data (temperature, humidity, and rainfall) based on location.
- *Responsive Design:* A user-friendly interface that works seamlessly on various devices.

## Technologies Used
- *Backend:* Django, Python
- *Frontend:* HTML, CSS, JavaScript
- *Machine Learning:* Scikit-learn (for crop recommendation model)
- *API Integration:* Weather API (for real-time weather data)

## Installation

### Prerequisites
- Python 3.x
- Django
- Pip

### Steps
1. *Clone the repository:*
    bash
    git clone https://github.com/yourusername/farmeasy.git
    cd farmeasy
    

2. *Create a virtual environment:*
    bash
    python3 -m venv env
    source env/bin/activate
    

3. *Install the required packages:*
    bash
    pip install -r requirements.txt
    

4. *Run database migrations:*
    bash
    python manage.py migrate
    

5. *Start the Django development server:*
    bash
    python manage.py runserver
    

6. *Access the application:*
   Open your web browser and go to http://127.0.0.1:8000/.

## Usage
1. *Home Page:* Navigate to the home page where you can input soil properties or let the system detect them based on your location.
2. *Get Location:* Click on the "Get Location" button to autofill soil properties and weather data.
3. *Predict Crop:* Submit the form to get a crop recommendation based on the input data.

## Folder Structure  
