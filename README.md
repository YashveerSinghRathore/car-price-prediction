**Car Price Prediction Model**
This project is a machine learning-based car price prediction system. It uses several car-related features such as brand, model, car age, mileage, fuel type, and transmission to predict the car's price. The model was trained using historical car price data and implemented in an interactive web app using Streamlit.

The trained machine learning model can be downloaded [here](https://drive.google.com/file/d/1QZFHMC9RUrJzIa7RoOyM1njMM8prV7jr/view?usp=sharing).

**Project Overview**
The Car Price Prediction Model is designed to estimate the price of a used car based on several key attributes. This project consists of two main parts:

Model Training: The machine learning model was trained using historical data of used cars in Google Colab. The model was built using a Random Forest Regressor and saved using the pickle library.
Model Deployment: An interactive web application was created using Streamlit, where users can input car details (brand, model, car age, etc.), and the app will provide a predicted price.

**Features**
Car Price Prediction: Users can input key car features (brand, model, mileage, etc.) and receive an estimated price for the car.
Model Training: The machine learning model is trained on various car features to predict accurate prices.
Interactive Web Application: The Streamlit web app provides an easy-to-use interface for users to interact with the model.
Feature Importance: Shows the importance of each feature (e.g., car age, mileage) in determining the car price.

**Tools Used**
Python: Programming language used for the entire project.
Google Colab: For training the machine learning model.
Scikit-learn: Machine learning library used to implement the Random Forest Regressor.
Pandas & NumPy: Libraries used for data manipulation and numerical computations.
Streamlit: Used for creating the interactive web app.
Pickle: Used for saving and loading the trained machine learning model.

**Run the Project**
First, you can clone the repository to your local machine:

Install the mandetory packages
Navigate to the project directory and install the required Python packages using pip. Make sure you have Python installed:
Packages are:

streamlit
scikit-learn
pandas
numpy

Now You can Run the Streamlit Web App
Run the Streamlit app to interact with the car price prediction model:
streamlit run app.py

Once the app is running, input the following details:

Brand
Model
Car Age
Mileage (in Miles)
Fuel Type
Transmission Type
The model will use this data to predict the car's price.
