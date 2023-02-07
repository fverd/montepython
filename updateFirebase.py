import os

# folder path
dir = r'chains'
dir_path=os.path.join(os.path.expanduser("~"),'montepython',dir)
# list to store files
folders = {}
# Iterate directory
for path in os.listdir(dir_path):
    if os.path.isdir(os.path.join(dir_path, path)):

        chains={}
        # Iterate subdirectory
        for subpath in os.listdir(os.path.join(dir_path, path)):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path, subpath)):
                if subpath.endswith('.txt') and subpath.startswith('20'):

                    num_lines = sum(1 for line in open(os.path.join(dir_path, path, subpath)))
                    #subpath remove .txt
                    subpath = subpath.split('.')[0]
                    chains.update({subpath:num_lines})
        #path remove .txt
        path = path.split('.')[0]
        #print(path)
        folders.update({path:chains})

#folders to firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cert_path=os.path.join(os.path.expanduser("~"),'montepython',"montepythonmonitor-firebase-adminsdk-3c41y-9afd053eea.json")
cred = credentials.Certificate(cert_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://montepythonmonitor-default-rtdb.europe-west1.firebasedatabase.app/'
})

ref = db.reference('/chains')
ref.set(folders)

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
ref = db.reference('/timestamp')
ref.set(dt_string)
