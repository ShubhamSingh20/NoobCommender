#sklearn 
from sklearn.externals import joblib
from sklearn import preprocessing

#sklearn models
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#maths
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

# os
import os
import ast
import warnings
import time

#error
from sklearn.metrics import mean_squared_error

#SKlearn Stuff..
encoder = preprocessing.LabelEncoder()
model = NearestNeighbors(n_neighbors=2,metric='cosine',algorithm="brute",p=2)
kmean = KMeans(init='k-means++', n_clusters=5, n_init=10)

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'development')

DATASET_DIR = os.path.join(os.path.join(BASE_DIR,'dataset'),'final')
STORAGE_DIR = os.path.dirname(os.path.abspath(__file__)).replace('development','storage')

DATASET_FILE_NAME = "FINAL_DATASET_G.csv"
LABEL_FILE_NAME = "labels_1.csv"

global x_train,Y,temp_Y,temp_X


def get_labels(*args):
    df = pd.read_csv(os.path.join(DATASET_DIR,LABEL_FILE_NAME),\
            usecols=['labels'])

    labels = df['labels']
    
    encoder.fit(labels)

    if args[1]:
        GARBAGE = [
        'jan','feb','march','april','apr','may','june','jul','aug',
        'oct','sept','nov','dec17','cook','acm','kgp','ltime','mhammad1','icop','cole','corp','isaf','gsf',
        'chemthan','chn','gwr17rol','keteki','icl','#editorial',' taran','cook97','taran_1407','com','codr2018','killjee',
        'jitendersheora','adlet_zeineken','aparup_ghosh','allllekssssa','inso','codh2018','hruday968','2-sat','kingofnumbers'
        ]
        storage_class_name = "unique_columns.pkl"
        garbage_column_class = "garbage_data.pkl"
        storage_class_name = os.path.join(STORAGE_DIR,storage_class_name)
        garbage_column_class = os.path.join(STORAGE_DIR,garbage_column_class)
        joblib.dump(labels,storage_class_name)
        joblib.dump(GARBAGE,garbage_column_class)


    if args[0]:
        for enocdings in encoder.classes_:
            print("Original : {}  Enocoding : {}".format(enocdings,encoder.transform([enocdings])))

def load_data():
    global x_train,Y,temp_Y,temp_X
    get_labels(False,True)
    df = pd.read_csv(os.path.join(DATASET_DIR,DATASET_FILE_NAME),converters={'tags' : pd.eval})

    Y = df['accuracy'].values
    temp_Y = df['accuracy'].values
    Y = Y.reshape(-1,1)

    tag_column = df['tags'].values
    temp_X = df['tags'].values
    vec_n = len(encoder.classes_)
    x_train = np.zeros((Y.shape[0],vec_n))

    for index,tag_list in enumerate(tag_column):
        tag_encoded = encoder.transform(tag_list)
        for encode in tag_encoded:
            x_train[index][encode] = Y[index][0]
   


def train_model(ratings,pred,**kwargs):
    model.fit(ratings)

    if "save" in kwargs:
        storage_class_name = kwargs.get("save")
        storage_class_name = os.path.join(STORAGE_DIR,storage_class_name)
        joblib.dump(model,storage_class_name)
        
    distances,indices = model.kneighbors(pred)
    similarities = 1-distances.flatten()
    score = np.mean(similarities)
    score = np.multiply(100,score)
    print("Similarity Score : %4f" % score)

    return indices

def kmeans_make_plot(**kwargs):
    global Y
    kmean.fit(Y)
    if "save" in kwargs:
        storage_class_name = kwargs.get("save")
        storage_class_name = os.path.join(STORAGE_DIR,storage_class_name)
        joblib.dump(kmean,storage_class_name)

    centroids = kmean.cluster_centers_
    plt.scatter(np.arange(Y.shape[0]),Y,c=kmean.labels_)
    plt.scatter(centroids,centroids,marker='x',c='r',linewidths=1,s=169)
    
    plt.title('K-means clustering on the CodeChef(Accuracy)')
    plt.xlabel('Samples')
    plt.ylabel('Accuracy')
    plt.show()

def get_kmeans_clusters(save=True):
    global temp_Y,temp_X
    cluster_map = pd.DataFrame()
    cluster_map['accuracy'] = temp_Y
    cluster_map['cluster'] = kmean.labels_
    print(encoder.inverse_transform(np.nonzero(x_train.all())))
    cluster_map['tags'] = temp_X

    cluster_map.to_csv(os.path.join(DATASET_DIR,'cluster_map.csv'))

def joblib_kmeans_cluster():
    n_clusters = 5
    df = pd.read_csv(os.path.join(DATASET_DIR,'cluster_map.csv'))

    for i in range(n_clusters):
        joblib.dump(df[df.cluster == i],os.path.join(STORAGE_DIR,"cluster_{}".format(i+1)))

def main():
    load_data()
    train_model(x_train[:445],x_train[445:],save="Knn_search.pkl")
    kmeans_make_plot()
    get_kmeans_clusters()
    joblib_kmeans_cluster()

if __name__ == '__main__':
    main()
