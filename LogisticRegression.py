from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

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
print("Accuracy: ", Score*100, "Percent")

PatientCT=int(input("Enter The Clump Thickness: "))
PatientUCSize=int(input("Enter The Uniformity Of Cell Size: "))
PatientUCShape=int(input("Enter The Uniformity Of Cell Shape: "))
PatientMA=int(input("Enter The Uniformity Of Marginal Adhesion: "))
PatientSECS=int(input("Enter The Uniformity Of Single Epithelial Cell Size: "))
PatientBN=int(input("Enter The Bare Nuclei: "))
PatientBC=int(input("Enter The Bland Chromatin: "))
PatientNN=int(input("Enter The Normal Nucleoli: "))
PatientMitosis=int(input("Enter The Mitosis: "))

Predict=model.predict([[PatientCT, PatientUCSize, PatientUCShape, PatientMA, PatientSECS, PatientBN, PatientBN, PatientNN, PatientMitosis]])

if (Predict==2):
    print("Benign")
else:
    print("Malignant")
