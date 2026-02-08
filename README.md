# Bank Marketing Classification

## Project Overview
This project aims to predict whether a bank client will subscribe to a term deposit based on demographic and marketing campaign information.  
It is a supervised machine learning binary classification problem.

The project covers the complete data science workflow including data preprocessing, exploratory data analysis (EDA), model training, and evaluation.

---

## Dataset
- Dataset Name: Bank Marketing Dataset  
- Source: UCI Machine Learning Repository  
- File Used: bank-full.csv  
- Target Variable: y (yes / no)

---

## Project Structure
bank-marketing-classification/
├── notebooks/
│   └── bank_marketing_eda_model.ipynb
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── evaluate.py
├── data/
│   └── data_reference.txt
├── README.md
└── requirements.txt

---

## Data Preprocessing
- Separated features and target variable
- Encoded categorical variables using One-Hot Encoding
- Scaled numerical features
- Split data into training and testing sets

---

## Exploratory Data Analysis
EDA was performed to understand feature distributions, class imbalance, and relationships between variables and the target.

---

## Model
Logistic Regression was used as a baseline classification model.

---

## Author
Umer Zaheer Lodhi