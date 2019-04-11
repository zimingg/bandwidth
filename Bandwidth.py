import urllib.request
import time as timer
import os
import sys


def MeasureBandwidth(url):
    # check if input is a valid url
    try:
        request = urllib.request.Request(url)
    except:
        print("Input is not a valid url!")
        raise Exception
       
    start = timer.time() 

    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        print("URL Error! Error Number: {}, Reason: {} ".format(e.code, e.reason))
        raise Exception
    
    content = response.read()
    end = timer.time() 
    time_used = end-start
    #convert byte to kb
    size = sys.getsizeof(content)/1000
    speed = size//time_used

    return int(speed)


def main():
    #check if url is entered
    if len(sys.argv) <= 1: #nothing entered
        print("No url entered!")
    else:
        try:
            speed = MeasureBandwidth(sys.argv[1])
            print("Bandwidth: {}kb/s ".format(speed))
        except:
            print("Please try again!")
       

if __name__ == "__main__":
    main()
    