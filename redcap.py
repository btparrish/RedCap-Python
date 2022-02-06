import pandas as pd
import json

#defines the python object Project which serves as a holder of information regarding a RedCap API connection
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
        return r.json()
    #accepts a list of RedCap record IDs to be deleted from the project. This input must be in the form of a Python list, and user must have correct permissions to delete record.
    def delete_record(self,records):
        data = {
        'token': self.token,
        'action': 'delete',
        'content': 'record',
        }
        records_dict = { f"records[{idx}]": record for idx, record in enumerate(records)}
        data.update(records_dict)
        r = requests.post('https://cri-datacap.org/api/',data=data)
        print('HTTP Status: ' + str(r.status_code))
        print(r.text)
    #Deletes all records in the RedCap project. Prompts the user to confirm their desire to delete all records in the project to prevent erroneous record deletion.
    def delete_all_records(self):
        data = {'token': self.token,
        'content': 'generateNextRecordName'
        }
        r = requests.post(self.url,data=data)
        next_record_int = int(r.text)
        user_spec = input("Are you sure you want to delete all the records in this project? This action cannot be undone (y/n): ")
        if user_spec.lower() == "y":
            for i in range(next_record_int):   
                data = {
                'token': self.token,
                'action': 'delete',
                'content': 'record',
                }
                records_dict = {"records[0]":str(i)}
                data.update(records_dict)
                r = requests.post('https://cri-datacap.org/api/',data=data)
                print('HTTP Status: ' + str(r.status_code))
                print(r.text)

        
        






        
                                                
