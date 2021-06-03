from flask import Flask, render_template, request
import pickle
from joblib import load
import sys
sys.path.insert(0, r'C:\Users\Aiden\Documents\Data_Science_Stuff\sf_Data_Science_Stuff\Projects\01_SportsNewsClassifier\final_code')
from data_prep.data_processing import make_prediction

model = load('final_model.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    headline = str(request.form.values())
    predict = make_prediction(model, headline)
    return render_template('predict.html',
        prediction_text = 'News headline category is: {}'.format(predict)
        )

