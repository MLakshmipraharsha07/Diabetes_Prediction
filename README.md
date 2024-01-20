# Diabetes Prediction:
This repository contains a machine learning model for predicting whether a person is diabetic or not. The model is integrated into a web application using Flask, allowing users to interact with it through a user-friendly interface.

## Overview:
The machine learning model is trained on a dataset containing relevant features such as age, BMI, blood pressure, and glucose levels. It leverages with framework like scikit-learn to achieve accurate predictions. The model is then integrated into a Flask web application, providing a seamless and accessible way for users to make predictions.

### Context
The dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset.

## Features:
**Diabetes Prediction Model:** A trained machine learning model that takes input parameters and predicts the likelihood of a person being diabetic.<br>
**Flask Web Application:** A user interface created with Flask that allows users to input their information and receive predictions in real-time.

## About the Dataset:
The dataset consists of several features like number of pregnancies, BMI, Age, Blood Pressure, Insulin level, Glucose level, Diabetes Pedigree Function and the target variable the outcome i.e. is the person suffering from diabetes (1) or not (0).
### Columns
- **Pregnancies:** Number of times pregnant<br>
- **Glucose:** Plasma glucose concentration a 2 hours in an oral glucose tolerance test<br>
- **Blood Pressure:** Diastolic blood pressure (mm Hg)<br>
- **SkinThickness:** Triceps skinfold thickness (mm)<br>
- **Insulin:** 2-Hour serum insulin (mu U/ml)<br>
- **BMI:** Body mass index (weight in kg/(height in m)²)<br>
- **DiabetesPedigreeFunction:** It provided some data on diabetes mellitus history in relatives and the genetic relationship of those relatives to the patient.<br>
- **Age:** Age (years)<br>
- **Outcome:** Class variable (0 or 1) 268 of 768 is 1, the others are 0<br>

You Can Download the Dataset by clicking the link : [Dataset Link](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database).

## Steps Performed to Build the Machine Learning Model:

1. Create a Dataframe from the dataset
2. Perform Exploratory Data Analysis 
3. Consider the data into features and Target(splice into input and output)
4. Split data into training and testing
5. Perform preprocessing (if required)
6. Apply ML algorithm (using Sklearn library) for the above training data
7. Predict for Testing Data
8. Evaluate the test result by considering Accuracy Score, Confusion Matrix
9. Model Serialization into a pickle file

## Project Structure:

Diabetes_Prediction(root)<br>
&nbsp;&nbsp;&nbsp;|____templates<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|___index.html<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|___result.html<br>
&nbsp;&nbsp;&nbsp;|____static<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|____css<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|_____js<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|_____images<br>
&nbsp;&nbsp;&nbsp;|____app.py<br>
&nbsp;&nbsp;&nbsp;|_____Diabetes.pkl<br>
&nbsp;&nbsp;&nbsp;|____diabetes.csv<br>
&nbsp;&nbsp;&nbsp;|____diabetes.ipynb<br>

# Getting Started:
To run the web application locally, follow these steps:<br>
**1. Clone the Repository:** <br>
git clone https://github.com/MLakshmipraharsha07/Diabetes_Prediction.git<br>
cd Diabetes_Prediction<br>
OR<br>
Download the zip file and extract the files in your local system.

**2. Install Dependencies:** <br>
pip install -r requirements.txt

**3. Pickle File for model serialization:** <br>
Download the serialized model file (pickle file) and place it in the Diabetes_Prediction/ directory.

**4. Run the Web Application:** <br>
1. Run the Flask Application <br>
python app.py<br>
2. Visit http://127.0.0.1:5000/ in your web browser. or You can just click the live server link that is generated in the terminal when the app.py file is executed.<br>

# Usage:
1. Open the web application in your browser.
2. Enter the required information (e.g., age, BMI, blood pressure, glucose levels).
3. Click the "Predict" button.
4. The application will display the predicted result, indicating whether the person is diabetic or not.

# Output of the webpage:
![Home Page](https://github.com/MLakshmipraharsha07/Diabetes_Prediction/assets/98521185/a89cbd87-2825-48cd-8ebc-5e7d0978b32f)

![Enter Values](https://github.com/MLakshmipraharsha07/Diabetes_Prediction/assets/98521185/eb5aa5fd-d3ca-45bc-a714-ec85a195dc77)

![Diabetic Person](https://github.com/MLakshmipraharsha07/Diabetes_Prediction/assets/98521185/c779da16-b19e-432a-b05f-d5263cab53b3)

![Non Diabetic Person](https://github.com/MLakshmipraharsha07/Diabetes_Prediction/assets/98521185/051862bd-cbc5-4dc6-a215-fd6c3a02585a)

## Demo Video of the Webpage:

https://github.com/MLakshmipraharsha07/Diabetes_Prediction/assets/98521185/09958cc6-3bc9-4771-b8bc-37003607e094




