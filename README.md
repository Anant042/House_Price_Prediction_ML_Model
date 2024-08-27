# House Price Prediction Using Regression

This project is an implementation of a regression model to predict house prices based on location, number of bedrooms (BHK), bathrooms, and area. The project uses several regression algorithms, including Lasso and DecisionTreeRegressor, with the best model being selected using GridSearchCV. The application is built using Flask, and the API can be run locally.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Selection](#model-selection)

## Introduction

This project predicts house prices using a regression model trained on various features, such as location, BHK, bathrooms, and area. The application provides an API, built using Flask, that runs on a local server and can be accessed through a web interface.

## Features

- House price prediction based on location, BHK, bathrooms, and area
- Multiple regression models with hyperparameter tuning
- Lightweight Flask application
- JSON-based API responses

## Technologies Used

- Python
- Jupyter Notebook
- Flask
- Scikit-learn
- Pandas
- Numpy

## Dataset

- Download data from [Kaggle](https://www.kaggle.com/datasets) (specify the dataset URL as needed)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    ```
2. **Navigate to the project directory:**
    ```sh
    cd your-repo-name
    ```
3. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask app:**
    ```sh
    python app.py
    ```
2. **Access the API:**
    Open your web browser or API client and navigate to `http://127.0.0.1:5000/`.

3. **User Interface:**
    After running `app.py` and navigating to the provided link, a template file will be executed that takes you to the user interface created using HTML and CSS. Here, you can input the location, BHK, bathrooms, and area to predict the house price.

## API Endpoints

- **`/predict`**: Accepts input features (location, BHK, bathrooms, area) and returns the predicted house price.

## Model Selection

The following algorithms were used in the project, with the best model selected using GridSearchCV:

- **Linear Regression**: Simple linear model
- **Lasso Regression**: Linear model with L1 regularization
- **Decision Tree Regressor**: Non-linear model with tree-based approach


