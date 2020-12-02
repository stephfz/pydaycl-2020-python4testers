import json
import requests

class AuthorizationService(object):

    def __init__(self, base_url, service):
        self.header = {'cache-control': "no-cache", 'content-type': "application/json"}
        self.base_url = base_url
        self.service_url = service

    def authorize_user(self, username, password):
        data = {"username": username, "password" : password}
        url = "{0}/{1}".format(self.base_url,self.service_url)
        r = requests.post(url, data = data)
        return r
