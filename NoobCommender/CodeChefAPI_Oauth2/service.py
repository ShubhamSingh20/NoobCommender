from django.shortcuts import redirect
from urllib.request import urlopen
from django.http.request import HttpRequest
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

from CoreEngine.models import SolvedProblems
from .import errors
import logging
import requests
import urllib
import uuid
import json


CLIENT_ID = "<CLIENT ID>"
CLIENT_SECRET = "<CLIENT SECRET>"

API_URL = "https://api.codechef.com/"

DOMAIN_URL = "<DOMAIN URL>"
REDIRECT_URI = "<REDIRECT URI>"


class FetchAPIresponse:
    def __init__(self,**kwargs):
        self.auth_token = kwargs.get("auth_token",None)
        self.refresh_token = kwargs.get("refresh_token",None)
        self.access_token = kwargs.get("access_token",None)

    @staticmethod
    def get_authentication_code():
        temp_state = uuid.uuid4().hex
        auth_url = "{0}oauth/authorize?".format(API_URL)
        
        params = {
            "client_id": CLIENT_ID,
			"response_type": "code",
			"state": temp_state,
			"redirect_uri": REDIRECT_URI,
		}

        req = requests.Request('POST',url=auth_url,\
            params=urllib.parse.urlencode(params)).prepare()

        try:
            return redirect(req.url)
        except (requests.ConnectionError,requests.Timeout) as e:
            raise errors.Unavailable() from e
        
    def get_access_token(self):

        headers = {
            "content-Type": "application/json",
            "X-Accept":"application/json",
        }
        params = {
            "grant_type":"authorization_code",
            "code":self.auth_token,
            "client_id":CLIENT_ID,
            "client_secret":CLIENT_SECRET,
            "redirect_uri":REDIRECT_URI,
        }

        try:
            response = requests.post(
                API_URL+'oauth/token',
                data = json.dumps(params),
                headers=headers
            )

        except (requests.ConnectionError,requests.Timeout) as e:
            raise errors.Unavailable() from e
        try:
            return response.json()['result']['data']    
        except:
            print(response.json())
        

    def make_requests(self,get_url):
        
        comm = "Bearer {}".format(self.access_token)
        headers = {
            "Accept": "application/json",
            "Authorization":comm,
        }   

        try:
            response = requests.get(get_url,headers=headers)
        except (requests.ConnectionError,requests.Timeout) as e:
            raise errors.Unavailable() from e

        try:
            response = response.json()['result']['data']['content']
        except:
            print(response)
            logger.info(response)
            return

        return response

    def get_new_access_from_refresh_token(self):
        headers = {
            "content-Type":"application/json",
        }
        
        params = {
            "grant_type":"refresh_token",
            "refresh_token":self.refresh_token,
            "client_id":CLIENT_ID,
            "client_secret":CLIENT_SECRET,
        }

        try:
            response = requests.post(
                API_URL + 'oauth/token',
                data = json.dumps(params),
                headers=headers
            )
        except (requests.ConnectionError,requests.Timeout) as e:
            raise errors.Unavailable() from e

        try:
            return response.json()['result']['data']
        except:
            pass
        

class CodeChefAPIUtitlity(FetchAPIresponse):
    #Use tags to get Questions
    def __init__(self,**kwargs):
        self.access_token = kwargs.get("access_token")
        self.refresh_token = kwargs.get("refresh_token")
    
    TAG_PROBLEM_URL = "https://api.codechef.com/tags/problems?filter={}&fields={}&limit={}&offset={}"
    CONTEST_CODE_URL = "https://api.codechef.com/contests/{}/problems/{}?fields={}"
    TODO_URL = "https://api.codechef.com/todo/add"

    LIMIT,OFFSET,FIELD = 20,0,'code'
    DEFAULT_TAGS = ['easy']
    API_REQUEST_LIMIT = 30


    def get_questions_(self,tag_list,default=False):
        if default:
            self.LIMIT = 20
            tag_list = self.DEFAULT_TAGS

        self.TAG_PROBLEM_URL = self.TAG_PROBLEM_URL.format(
            ','.join(tag_list),
            self.FIELD,
            self.LIMIT,
            self.OFFSET
        )
        FetchAPIresponse.__init__(self,refresh_token=self.refresh_token,access_token=self.access_token)
        return self.make_requests(self.TAG_PROBLEM_URL)

    def get_tags_(self,problem_code,contest_code = 'PRACTICE'):
        self.CONTEST_CODE_URL = self.CONTEST_CODE_URL.format(
            contest_code,
            problem_code,
            'tags'
        )
        FetchAPIresponse.__init__(self,refresh_token=self.refresh_token,access_token=self.access_token)
        return self.make_requests(self.CONTEST_CODE_URL)
        

    def add_TODO(self,problem_code,contest_code='PRACTICE'):

        comm = "Bearer {}".format(self.access_token)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            "Authorization":comm,
        }

        data = {
            'problemCode':problem_code,
            'contestCode':contest_code, 
        }
        FetchAPIresponse.__init__(self,get_url = self.TODO_URL,\
                    refresh_token=self.refresh_token,access_token=self.access_token)
        try:
            response = requests.post(self.TODO_URL,data=json.dumps(data),headers=headers)
        except (requests.ConnectionError,requests.Timeout) as e:
            raise errors.Unavailable() from e
        
        return response.json()