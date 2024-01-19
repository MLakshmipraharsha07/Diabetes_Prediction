#importing necessary libraries
from flask import Flask,request, url_for, redirect,render_template
import pickle #pickle for loading model(Diabetes.pkl)
import pandas as pd

app = Flask(__name__) #setting up flask name

model = pickle.load(open("Diabetes.pkl", "rb")) #loading model

@app.route('/')  #Defining the main index route
def home():
    return render_template('index.html')  #redirects to the index page of html

@app.route('/predict', methods=['POST','GET'])
def predict():
    text1 = request.form['1']      ## Fetching each input field value one by one
    text2 = request.form['2'] 
    text3 = request.form['3']
    text4 = request.form['4']
    text5 = request.form['5']
    text6 = request.form['6']
    text7 = request.form['7']
    text8 = request.form['8']
    
    row_df = pd.DataFrame([pd.Series([text1,text2,text3,text4,text5,text6,text7,text8])]) ### Creating a dataframe using all the values
    print(row_df)
    
    prediction = model.predict_proba(row_df) #Predicting the output
    result = '{0:.{1}f}'.format(prediction[0][1],2) #Formating output
    
    if result > str(0.5):
        return render_template('result.html',pred='The Person has a chance of diabeties.') ## Returning the message for use on the same index.html page
    else:
        return render_template('result.html',pred='You are safe.\n Probability of having diabetes is {}'.format(result)) 


if __name__ == '__main__':
    app.run(debug=True)          ## Running the app as debug==True