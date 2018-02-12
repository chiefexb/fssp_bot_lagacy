#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests

class FsspApi(object):
    base_url="https://api-ip.fssprus.ru/api/v1.0"
    def __init__(self,token):
        self.token=token
    
    def set_lastname(self,lastname):
        self.lastname=lastname

    def set_firstname(self,firstname):
        self.firstname=firstname

    def set_region(self,region):
        self.region=region

    def search_phisycal(self):
        
        req=requests.get(self.base_url+'/search/physical',params=
        {'token'    :self.token,
         'region'   :self.region,
         'firstname':self.firstname,
         'lastname' :self.lastname})
        if (req.status_code==200):
            self.task=req.content['task']
        self.r_status=req.status_code
        
    def get_status_task(self):
        
        req=requests.get(self.base_url+'/status',params=self.par)
        if req.status_code==200:
           self.status=req.content
        self.r_status=req.status_code
    
def main():
   pass
if __name__ == "__main__":
    main()
