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

        #fully read through the file and count the size as kb.
        size = 0
        while response.read(1000):
            size+=1

        end = timer.time() 

        if size < 100:
            print("NOTICE: URL file size is smaller than 100kb, the result might not be accurate.")

        time_used = end-start
        speed = size/time_used

        return int(speed)