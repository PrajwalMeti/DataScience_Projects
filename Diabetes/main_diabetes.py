import numpy as np 
import pandas as pd 
from fastapi import FastAPI
from pydantic import BaseModel  
import pickle 

class InputRequest(BaseModel):    
    Pregnancies  : int
    Glucose :  int
    BloodPressure :  int
    SkinThickness :  int
    Insulin        :   int
    BMI             :  int
    DiabetesPedigreeFunction : int
    Age  : int



app = FastAPI()

@app.get('/')
def diabetes_predection_app():
    return 'Hello World' 
 
@app.post('/diabetes/predict')
def predict(input:InputRequest):   
    with open('logreg.pkl','rb') as f:  
        model = pickle.load(f) 
 
    output =  model.predict(np.array([input.Pregnancies,
                                    input.Glucose, 
                                    input.BloodPressure,
                                    input.SkinThickness,
                                    input.Insulin,  
                                    input.BMI,  
                                    input.DiabetesPedigreeFunction,
                                    input.Age]).reshape(1,-1)).tolist()
    if output[0] == 1:
        return 'You have Diabeties! Please Take Care'
    else :
        return "You don't Have Diabeties! Enjoy your Life"