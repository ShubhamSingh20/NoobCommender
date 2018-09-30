from django.shortcuts import redirect
from urllib.request import urlopen
from django.http.request import HttpRequest
import errors
import logging
import requests
import urllib
import uuid
import json

CLIENT_ID = "<CLIENT ID>"
CLIENT_SECRET = "<CLIENT SECRET>"

API_URL = "https://api.codechef.com/"

DOMAIN_URL = "http://127.0.0.1:8000/"
REDIRECT_URI = "http://127.0.0.1:8000/oauth/"


class FetchAPIresponse:
    def __init__(self,**kwargs):
        self.auth_token = kwargs.get("auth_token",None)
        self.refresh_token = kwargs.get("refresh_token",None)
        self.access_token = kwargs.get("access_token",None)
        self.get_url = kwargs.get("get_url",None)

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
       
        return response.json() 

    def make_requests(self):
        
        comm = "Bearer {}".format(self.access_token)
        headers = {
            "Accept": "application/json",
            "Authorization":comm,
        }

        try:
            response = requests.get(self.get_url,headers=headers)
        except (requests.ConnectionError,requests.Timeout) as e:
            raise errors.Unavailable() from e

        return response.json()

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
        
        return response.json()

class UpdateDjangoObjects(object):

    @classmethod
    def update_user_attribute(cls,current_user,**kwargs):
        if 'first_name' in kwargs and 'last_name' in kwargs:
            current_user.first_name = kwargs.get('first_name')
            current_user.last_name = kwargs.get('last_name')

        current_user.refresh_token = kwargs.get('refresh_token')
        current_user.access_token = kwargs.get('access_token')
        current_user.save()
        
        return current_user

    @classmethod
    def save_user_contest_details(cls,cur_user_,**kwargs):
        return cur_user_

        

        





