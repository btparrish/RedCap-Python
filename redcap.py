import pandas as pd
import json

class Project(object):
    def __init__(self, url, token):
        self.token = token
        self.url = url

    def next_record(self):
        data = {'token': self.token,
        'content': 'generateNextRecordName'
        }
        r = requests.post(self.url,data=data)
        return r.text

    def write_record(self,record_to_write):
        data = {'token': self.token,
        'content':'record',
        'action':'import',
        'format':'json',
        'type':'flat',
        'overwriteBehavior':'normal',
        'forceAutoNumber':'false',
        'data':"{}".format(json.dumps([record_to_write])),
        'returnContent':'count',
        'returnFormat':'json'
        }
        r = requests.post(self.url,data=data)
        return r.json()
    def get_survey_link(self,record):
        data = {
        'token': self.token,
        'content': 'surveyLink',
        'format': 'json',
        'instrument': '',
        'event': '' ,
        'record': '{}'.format(str(record)),
        'returnFormat': 'json'
        }
        r = requests.post('https://cri-datacap.org/api/',data=data)

        
        






        
                                                
