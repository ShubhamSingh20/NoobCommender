import pandas as pd 
import numpy as np 

DATAFILE_NAME_1 = "cleaned_dataset.csv"
DATAFILE_NAME_2 = "cleaned_dataset_2.csv"

a = pd.read_csv(DATAFILE_NAME_1)
b = pd.read_csv(DATAFILE_NAME_2)

import os
add = os.path.join(os.getcwd(),"FINAL_DATASET_G.csv")
#print(add)
frames = [a,b]
df = pd.concat(frames)

try:
    df.to_csv(add)
except:
    print("something happend")


dfn = pd.read_csv(add)
print(dfn)