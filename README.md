# Advanced House Price Prediction using Linear Regression

## Project Overview

This project predicts house sale prices using the Ames Housing dataset.
The goal is to build a regression model that estimates house prices based on important features such as house size, quality, garage capacity, and age.

The model is trained using Linear Regression and deployed using a Streamlit web application.

---

## Dataset

Dataset used: **Ames Housing Dataset**

Files used:

* train.csv
* test.csv
* data_description.txt

Source: Kaggle – House Prices Advanced Regression Techniques

---

## Problem Statement

Predict the sale price of a house based on different house features.
This helps buyers, sellers, and real estate companies estimate property prices.

---

## Feature Engineering

New features were created to improve prediction performance:

**TotalArea**
Total Area = Basement Area + 1st Floor Area + 2nd Floor Area

**HouseAge**
House Age = Current Year − Year Built

---

## Model Used

Linear Regression

The dataset was split into:

* 80% Training Data
* 20% Testing Data

---

## Model Evaluation

The model was evaluated using the following metrics:

**RMSE (Root Mean Squared Error)**
Measures prediction error.

**R² Score**
Shows how well the model explains the data.

---

## Deployment

The trained model was deployed using Streamlit.

Users can enter house details such as:

* Overall Quality
* Living Area
* Garage Capacity
* Total Area
* House Age

The app then predicts the estimated house price.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Streamlit
* VS Code
* GitHub

---

## Project Structure

```
house-price-prediction
│
├── train.csv
├── test.csv
├── task.ipynb
├── house_price_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## How to Run the Project

Install dependencies:

```
pip install -r requirements.txt
```

Run Streamlit app:

```
streamlit run app.py
```

---

## Output

The model predicts the estimated sale price of a house based on user input features.

---
## Live App
Streamlit Deployment:https://tejaswinib004-cpu-house-price-prediction-regression-app-gj6tmp.streamlit.app/

## Author

Tejaswini Bollaboina

