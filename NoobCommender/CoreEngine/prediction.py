from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib

from ast import literal_eval
import numpy as np 
import pandas as pd  
import json
import os

print("Loading Model .... !")
    

class MLModel:
    MODEL_NAME = "Knn_search.pkl"
    UNIQUE_TAGS = "unique_tags.pkl"
    GARBAGE_DATA = "garbage_data.pkl"

    BASE_DIR = os.path.dirname(os.path.abspath(__package__)).replace("NoobCommender","Core")
    STORAGE_DIR = os.path.join(BASE_DIR,'storage')
    
    def __init__(self,**kwargs):
        self.band_id = kwargs.get('band')
        self.cluster = joblib.load(os.path.join(self.STORAGE_DIR,'cluster_band_{}'.format(self.band_id)))
        
    @staticmethod
    def stringToList(string):
        string = string[1:len(string)-1]
        try:
            if len(string) != 0: 
                tempList = string.split(", ")
                newList = list(map(lambda x: literal_eval(x), tempList))
            else:
                newList = []
        except:
            newList = [-9999]
        return (newList)

    def get_tags(self,**kwargs):
        #self.cluster["tags"] = self.cluster["tags"].apply(lambda x: self.stringToList(x))
        try:
            elem = self.cluster['tags'][kwargs.get("index")]
        except:
            elem -1
        
        return elem
        
       
        
def fetch_tags(request):

    user = request.user
    mLmodel = MLModel(band=user.band)
    q_index = user.q_index

    tag_list = mLmodel.get_tags(index = q_index)
    if tag_list == -1:
        return tag_list
        
    user.q_index = q_index + 1
    user.save()
    return (tag_list,q_index+1)
