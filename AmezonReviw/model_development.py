import pandas as pd 
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,f1_score,recall_score,precision_score,confusion_matrix
from sklearn.pipeline import Pipeline
from fastapi import FastAPI
from pydantic import BaseModel
import joblib 

class InputRequest(BaseModel):
    Review : str


app = FastAPI()

@app.post('/amezonreview/sentimentalanalysis')
def sentimantal(input:InputRequest):
    with open('3rd_model_pipeline.pk','rb') as f:
        model = joblib.load(f) 
  
    output = model.predict([input.Review]) 

    if output[0] == 1:
         return 'Postive'
    else:
         return 'Negative'    
      
