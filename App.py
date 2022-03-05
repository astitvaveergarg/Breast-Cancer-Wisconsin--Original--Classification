from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect
from forms import Prediction
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Predictions'

@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/Prediction', methods=['GET', 'POST'])
def Prediction_Page():
    form = Prediction()
    if form.is_submitted():
            global result 
            result = request.form
            return redirect('/Predicted')
    return render_template("form.html", form=form)


@app.route('/Predicted')
def Predicted_Page():
    dataset=pd.read_csv(r'D:\GIT\Breast-Cancer-Wisconsin--Original--Classification\breast-cancer-wisconsin.csv')

    ClumpThickness= np.array(dataset['CT'].values).reshape(-1,1)
    UniformityOfCellSize= np.array(dataset['UCSize'].values).reshape(-1,1)
    UniformityOfCellShape= np.array(dataset['UCShape'].values).reshape(-1,1)
    MarginalAdhesion= np.array(dataset['MA'].values).reshape(-1,1)
    SingleEpithelialCellSize= np.array(dataset['SECS'].values).reshape(-1,1)
    BareNuclei= np.array(dataset['BN'].values).reshape(-1,1)
    BlandChromatin= np.array(dataset['BC'].values).reshape(-1,1)
    NormalNucleoli= np.array(dataset['NN'].values).reshape(-1,1)
    Mitoses= np.array(dataset['M'].values).reshape(-1,1)
    Class= np.array(dataset['C'].values)

    Features=np.concatenate((ClumpThickness, UniformityOfCellSize, UniformityOfCellShape, MarginalAdhesion, SingleEpithelialCellSize, BareNuclei, BlandChromatin, NormalNucleoli, Mitoses),axis=1)

    model=LogisticRegression()
    model.fit(Features, Class)

    Score=model.score(Features, Class)
    Accuracy=round(Score*100, 2)

    PatientCT = result.get('PatientCT')
    PatientUCSize = result.get('PatientUCSize')
    PatientUCShape = result.get('PatientUCShape')
    PatientMA = result.get('PatientMA')
    PatientSECS = result.get('PatientSECS')
    PatientBN = result.get('PatientBN')
    PatientBC = result.get('PatientBC')
    PatientNN = result.get('PatientNN')
    PatientMitosis = result.get('PatientMitosis')

    Predict=model.predict([[PatientCT, PatientUCSize, PatientUCShape, PatientMA, PatientSECS, PatientBN, PatientBC, PatientNN, PatientMitosis]])

    if (Predict==2):
        predictedresult = "Benign"
        
    else:
        predictedresult = "Malignant"

    return render_template('Result.html', Tumour=predictedresult, Model_Accuracy=Accuracy)

if __name__=='__main__':
    app.run(debug=True)


