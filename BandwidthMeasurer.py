import urllib.request
import time as timer
import os
import sys

class BandwidthMeasurer:
    def Measure(self,url):
        # if input is an invalid url, raise ValueError
        request = urllib.request.Request(url)
        
        # if there is any error loading the url, raise urllib.error.HTTPError
        response = urllib.request.urlopen(request, timeout=10)

        start = timer.time() 
        
        #fully read through the file and count the size as kb.
        size = 0
        while response.read(1000):
            size+=1

        end = timer.time() 

        if size < 500:
            print("NOTICE: URL file size is too small (<500kb), the result might not be accurate.")

        time_used = end-start
        speed = size/time_used

        return int(speed)