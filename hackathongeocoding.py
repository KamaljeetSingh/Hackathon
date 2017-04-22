import requests
import json
import pandas as pd
from queue import Queue
from threading import Thread
from time import time


class Geocoding:

    def __init__(self,input_file,output_file):
        self.frame = pd.read_csv(input_file)
        #self.frame.head() #Testing
        self.baseurl="https://maps.googleapis.com/maps/api/geocode/json?"
        self.key="AIzaSyBjS9_-orNS7CrEdNzJLLV-mrGsNsqVasQ"
        self.q=Queue()
        self.results=[]
        self.outputfile=output_file
        self.startThreads()


    def getCityNames(self):
        self.cities=self.frame["States/UTs"].unique().tolist()
        for c in self.cities:
            self.q.put(c)


    def getLongLat(self,i):
        while True:
            print('thread {} running'.format(i))
            resultdict={}
            resultdict['States/UTs']=self.q.get()
            payload={'address':resultdict['States/UTs'],'key':self.key}
            jsonstring=requests.get(self.baseurl,payload).text

            jsondict=json.loads(jsonstring)

            if jsondict['status']=='OK':
                resultdict['lat']=jsondict['results'][0]['geometry']['location']['lat']
                resultdict['long']=jsondict['results'][0]['geometry']['location']['lng']

            self.results.append(resultdict)
            print(self.results)
            self.q.task_done()


    def startThreads(self):
        ts=time()
        for i in range(4):
            t1=Thread(target=self.getLongLat, args=(i,))
            t1.setDaemon(True)
            t1.start()

        self.getCityNames()
        self.q.join()
        print("the process took {} seconds".format(ts-time()))
        self.update_Data()

    def update_Data(self):

        res=pd.DataFrame(self.results)
        updatedframe=pd.merge(self.frame,res,on='States/UTs',how='left',sort=False)
        updatedframe.to_csv(self.outputfile)



geo=Geocoding('updated_dstrIPC_1_2014.csv','updated_updated_dstrIPC_1_2014.csv')