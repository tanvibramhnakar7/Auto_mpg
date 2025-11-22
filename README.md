Auto MPG Prediction App 🚗⚡

This project is a Streamlit web application that predicts the Miles Per Gallon (MPG) of a car based on its features.
The prediction is powered by a machine learning model trained on the Auto MPG dataset.

📌 Features

Simple and user-friendly web interface

Takes horsepower, weight, and acceleration as input

Uses a pre-trained machine learning model (.pkl file)

Instantly displays MPG prediction

Easy to deploy on Streamlit Cloud / local machine

📂 Project Structure
📁 auto-mpg-app/
│── streamlit_app.py
│── model.pkl
│── requirements.txt
└── README.md

🧠 Model Details

The model is trained using the Auto MPG dataset.

It takes the following 3 features as input:

Feature	Description
horsepower	Engine horsepower rating
weight	Weight of the car in pounds
acceleration	Time taken to accelerate from 0–60 mph

Output: Predicted MPG (Miles Per Gallon)

🖥️ App Interface

The user enters:

Horsepower

Weight

Acceleration

Then clicks Predict, and the app displays the MPG value.

📦 requirements.txt

Typical contents:

streamlit
pandas
numpy
scikit-learn

🚀 Deployment

You can deploy the app easily on Streamlit Cloud:

Push project to GitHub

Go to https://share.streamlit.io

Connect repository

Select streamlit_app.py

Deploy
