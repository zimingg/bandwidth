import urllib.request
import time as timer
import os
import sys

def MeasureBandwidth(url):
    # check if input is a valid url
    try:
        request = urllib.request.Request(url)
    except:
        # print("invalid input!")
        raise ValueError("invalid input!")
    
    
    start = timer.time() 

    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        # print("Invalid url!")
        # print("Error Number: {}, Reason: {}".format(e.code, e.reason))
        raise ValueError("Invalid url! Error Number: {}, Reason: {}".format(e.code, e.reason))
        # return -1

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
        speed = MeasureBandwidth(sys.argv[1])
        if speed!=-1: 
            print("Bandwidth: {}kb/s ".format(speed))
        


if __name__ == "__main__":
    main()
    