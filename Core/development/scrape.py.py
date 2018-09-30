import service
import pandas as pd
import json
import numpy as np 
import os
import time


BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'Core')
DATASET_DIR = os.path.join(BASE_DIR,'dataset')

REFRESH_TOKEN =  '<CURRNET REFRESH TOKEN>'
TEMP_ACCESS_TOKEN = '<CURRENT ACCESS TOKEN>'

#URL = "https://api.codechef.com/users?fields=star&limit=20&offset=&search=av"

COLUMN_NAMES = ['Global Ranking','Problem Tags']

def get_tags():
    tags = []
    month_chal = [
        'Jan-','Feb','Mar','Apr','April','Aug','May','Jun','Jul','Sep','Sept','Oct','Nov','Dec','ltime','cook'
    ]
    data = service.FetchAPIresponse(access_token = TEMP_ACCESS_TOKEN,get_url=URL).make_requests()
    data = data['result']['data']['content']
    for attribure in data:
        elem = data[attribure]['tag'].replace(" ","")
        if data[attribure]['type'] != 'author':
            for month in month_chal:
                if month in elem:
                    print(elem)
                    elem = None
                    break

            if elem is not None:
                tags.append(elem)
    
    df = pd.DataFrame(tags,columns=[COLUMN_NAMES[1]])
    df.to_csv(os.path.join(DATASET_DIR,'problem_tags.csv'))


def get_contest_code():
    contest_code = []
    url = "https://api.codechef.com/contests?fields=&status=&offset=&limit=&sortBy=&sortOrder="
    data = service.FetchAPIresponse(access_token=TEMP_ACCESS_TOKEN,get_url=url).make_requests()
    data = data['result']['data']['content']['contestList']

    for attribute in data:
        contest_code.append(attribute['code'])
    
    df = pd.DataFrame(contest_code,columns=['contest_codes'])
    df.to_csv(os.path.join(DATASET_DIR,'contest_codes.csv'))

def get_contest_problem():
    dfContest = pd.read_csv(os.path.join(DATASET_DIR,'contest_codes.csv'),usecols=['contest_codes'])

    df = pd.DataFrame(columns=['contest_code','problem_code','successfulSubmissions','accuracy'])
    _refresh_token,_access_token = '<REFRESH TOKEN>',TEMP_ACCESS_TOKEN
    i=1
    for index,row in dfContest.iterrows():
        contest_codes = row['contest_codes']
        print(index,'refresh_token : ',_refresh_token, contest_codes)
        if index<800:
            url = "https://api.codechef.com/contests/{}?fields=&sortBy=&sortOrder=".format(contest_codes)
            data = service.FetchAPIresponse(access_token=_access_token,get_url=url).make_requests()
            if data['status'] == 'error':
                print(data)
                tokens_ = service.FetchAPIresponse(refresh_token=_refresh_token).get_new_access_from_refresh_token()['result']['data']
                _refresh_token = tokens_['refresh_token']
                _access_token = tokens_['access_token']
                
                data = service.FetchAPIresponse(access_token=_access_token,get_url=url).make_requests()
                print(data)
                
            try:
                data = data['result']['data']['content']
            except:
                df.to_csv(os.path.join(DATASET_DIR,'problem_details_{}.csv'.format(i)))  
                print("[+]Data saved... Last index : ",index-1)
                i+=1 
                print("[=]Process will wait now ...")
                time.sleep(60*5)
                data = service.FetchAPIresponse(access_token=_access_token,get_url=url).make_requests()
                print(data)
                data = data['result']['data']['content']
                print("[=]Process is back Online !")

            if data['problemsList']:
                problem_list = data['problemsList']
                for problems in problem_list:
                    df = df.append([{'contest_code':contest_codes,'problem_code':problems['problemCode'],'successfulSubmissions':problems['successfulSubmissions'],'accuracy':problems['accuracy']}])
        
    
def get_problem_details():
    dfProblem = pd.read_csv(os.path.join(DATASET_DIR,'problem_details_7.csv'),usecols=['contest_code','problem_code','successfulSubmissions','accuracy'])
    df = pd.DataFrame(columns=['contest_code','problem_code','successfulSubmissions','accuracy','tags'])
    _refresh_token,_access_token = '<REFRESH TOKEN>',""
    i=1
    for index,row in dfProblem.iterrows():
        contest_code = row['contest_code']
        problem_code = row['problem_code']
        print(index," Refresh token : ",_refresh_token)

        if index<60:
            url = "https://api.codechef.com/contests/{}/problems/{}?fields=tags".format(contest_code,problem_code)
            data = service.FetchAPIresponse(access_token=_access_token,get_url=url).make_requests()

            if data['status'] == 'error':
                print(data)
                tokens_ = service.FetchAPIresponse(refresh_token=_refresh_token).get_new_access_from_refresh_token()['result']['data']
                _refresh_token = tokens_['refresh_token']
                _access_token = tokens_['access_token']
                data = service.FetchAPIresponse(access_token=_access_token,get_url=url).make_requests()
                print(data)


            try:
                data = data['result']['data']['content']
            except:
                df.to_csv(os.path.join(DATASET_DIR,'final_details_{}.csv'.format(i)))  
                print("[+]Data saved... Last index : ",index-1)
                i+=1 
                print("[=]Process will wait now ...")
                time.sleep(60*5)
                data = service.FetchAPIresponse(access_token=_access_token,get_url=url).make_requests()
                print(data)
                data = data['result']['data']['content']
                print("[=]Process is back Online !")
            
            if data['tags']:
                tag_list = data['tags']
                df = df.append([{
                    'contest_code' : contest_code,
                    'problem_code' : problem_code,
                    'successful_submissions' : row['successfulSubmissions'],
                    'accuracy' : row['accuracy'],
                    'tags' : tag_list,
                }])
                print(df)
        else:
            df.to_csv(os.path.join(DATASET_DIR,'final_details_{}.csv'.format(i)))  
            print("[+]Data saved... Last index : ",index-1)
            break




if __name__ == '__main__':
    get_problem_details()
    #get_contest_problem()
    #get_contest_code()