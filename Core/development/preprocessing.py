import pandas as pd
import numpy as np 
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.join(BASE_DIR,'development')
DATASET_DIR = os.path.join(BASE_DIR,'dataset')
FINAL_DIR = os.path.join(DATASET_DIR,'final')

FILE_NAME = "final_details_pack_2_34.csv"
NEW_FILE_NAME = "FINAL_DATASET_G.csv"

COLUMNS = [
    'contest_code',
    'problem_code',
    'successful_submissions',
    'accuracy',
    'tags'
]

GARBAGE = [
    'jan','feb','march','april','apr','may','june','jul','aug',
    'oct','sept','nov','dec17','cook','acm','kgp','ltime','mhammad1','icop','cole','corp','isaf','gsf','dec16','cocr2016'
    'chemthan','chn','gwr17rol','keteki','icl','#editorial',' taran','cook97','taran_1407','com','codr2018','killjee',
    'jitendersheora','adlet_zeineken','aparup_ghosh','allllekssssa','inso','codh2018','hruday968','2-sat','kingofnumbers'
]


def load_data():
    dfLoad = pd.read_csv(os.path.join(FINAL_DIR,FILE_NAME),converters={'tags' : pd.eval})
    dfLoad = dfLoad.dropna(axis='columns')
    dfLoad = dfLoad.drop(dfLoad.columns[\
                dfLoad.columns.str.contains('unnamed',case = False)\
    ],axis = 1)
    return dfLoad


def remove_garbage_(tag_list):
    remove_i = []
    #Returns a list containing all the elements, which are garbage...
    for index,i in enumerate(tag_list):
        for j in GARBAGE:
            if j in i:
                try:
                    remove_i.append(i)
                except:
                    print(tag_list,"in",index)
    return remove_i


'''
    Returns a form of the dataset in 1*n vector,
    expanding the list into row element
'''
def write_changes():
    df = load_data()
    newDf = pd.DataFrame(columns=COLUMNS)
    tag_col = COLUMNS[4]

    df[tag_col] = [[i.lower() for i in tag_list]\
         for tag_list in df[tag_col][:]]
    
    for index,row in df.iterrows():
        accuracy = row['accuracy']
        contest_code = row['contest_code']
        problem_code = row['problem_code']
        successful_submissions = row['successful_submissions']

        tag_list = row['tags']
        new_tag_list = np.nan
        remove_tag_list = remove_garbage_(tag_list)

        if len(remove_tag_list)>0:
            new_tag_list = list(set(tag_list).difference(set(remove_tag_list)))
        else:
            new_tag_list = tag_list
        if not new_tag_list:
            print(new_tag_list)
        else:
                newDf = newDf.append([{
                    'contest_code':contest_code,
                    'problem_code':problem_code,
                    'successful_submissons':successful_submissions,
                    'accuracy':accuracy,
                    'tags':new_tag_list,
                }])
    print(newDf)
    newDf = newDf.drop(newDf.columns[\
                newDf.columns.str.contains('unnamed',case = False)\
    ],axis = 1)
    newDf = newDf.dropna(axis=1,how='all')
    newDf = newDf.dropna()
    newDf.to_csv(os.path.join(FINAL_DIR,NEW_FILE_NAME))


def get_all_labels():

    df = pd.read_csv(os.path.join(FINAL_DIR,NEW_FILE_NAME),converters={'tags' : pd.eval})
    merge = set()

    for _,row in enumerate(df.tags):
        merge |= set(row)
    
    merge = list(merge)
    print(merge)
    newDf = pd.DataFrame(merge,columns=['labels'])
    newDf.to_csv(os.path.join(FINAL_DIR,'labels_1.csv'))
    


if __name__ == '__main__':
    get_all_labels()
    write_changes()

    