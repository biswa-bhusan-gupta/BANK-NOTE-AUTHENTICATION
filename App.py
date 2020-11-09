from flask import Flask,request,render_template

import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)

Pickle_In=open('Bank_Note.pkl','rb')
Classifier=pickle.load(Pickle_In)

@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/Predict",methods=["POST"])
def Predict():
    if request.method == 'POST':
         Variance=float(request.form['variance'])
         Skewness=float(request.form['skewness'])
         Curtosis=float(request.form['curtosis'])
         Entropy=float(request.form['entropy'])

         Prediction=int(Classifier.predict([[Variance,Skewness,Curtosis,Entropy]]))
         if Prediction == 0:
             return render_template("Invalid.html",prediction_text=" Bank Note is Invalid")
         else:
             return render_template("Valid.html",prediction_text="Bank Note is Valid")
    return render_template("Index.html")

if __name__ == "__main__":
    app.run(debug=True)
