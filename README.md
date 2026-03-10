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
### Model Evaluation & Results

The baseline Logistic Regression model was evaluated to assess its performance in predicting term deposit subscriptions. 

* **Accuracy:** 90.16%
* **Classification Report Highlights:** * The model performed exceptionally well on the majority class (No Subscription) with an F1-score of 0.95.
  * Performance on the minority class (Subscription) yielded an F1-score of 0.44.
* **Key Findings:** While the overall accuracy is high at over 90%, the precision and recall metrics reveal a clear class imbalance. The model is heavily biased toward the majority class, indicating that overall accuracy alone is not the best metric for this specific business problem.
---
### Future Improvements

To further enhance the predictive power and address the complexities of this dataset, future iterations of this project could include:
* Applying techniques like SMOTE (Synthetic Minority Over-sampling Technique) or class weighting to handle the extreme class imbalance and improve predictions for true subscribers.
* Implementing advanced ensemble models such as Random Forest or Gradient Boosting (XGBoost) to capture non-linear relationships.
* Conducting rigorous hyperparameter tuning to optimize the macro F1-score rather than just baseline accuracy.
---
## Author
Umer Zaheer Lodhi
