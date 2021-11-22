import pandas as pd
import json

#defines the python object Project which serves as a holder if information regarding a RedCap API connection
#url is the default RedCap API endpoint https://cri-datacap.org/api/
#token is a unique redcap API key that is generated on a user and a project specific basis
class Project(object):
    #instantiates an object of the Project class that stores information regarding the API URL and the project's token ID
    def __init__(self, url, token):
        self.token = token
        self.url = url
    #returns the Record ID of the next record in the project to be written in sequential order. If most recent record is 5, this function returns 6
    def next_record(self):
        data = {'token': self.token,
        'content': 'generateNextRecordName'
        }
        r = requests.post(self.url,data=data)
        return r.text
    #accepts a Python data dictionary as an object with dictionary keys that correspond to survey variable names and values that correspond to what the responses will be
    #this function will write a Python data dictionary to redcap as a record after first converting it to a json object.
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
    #accepts a RedCap record ID for a preexisting survey record and returns the URL to complete that survey.
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

        
        






        
                                                
