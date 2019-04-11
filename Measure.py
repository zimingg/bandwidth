import urllib.request
import time as timer
import os
import sys

class MyMeasure:
    def MeasureBandwidth(self,url):
        # check if input is a valid url
        request = urllib.request.Request(url)
        
        start = timer.time() 

        # check if there is any error loading the url
        response = urllib.request.urlopen(request)

        #fully load the file
        content = response.read()

        end = timer.time() 

        time_used = end-start
        #convert byte to kb
        size = sys.getsizeof(content)/1000
        speed = size/time_used

        return int(speed)