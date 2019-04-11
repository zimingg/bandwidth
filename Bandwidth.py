import urllib.request
import time
import os
import sys

def MeasureBandwidth(url):
    #check if the input string is an url
    try:
        the_url = urllib.request.Request(url)
    except:
        print("invalid input!")
        return -1
    
    
    start = time.time() #start record time

    #open the url
    try:
        url_file = urllib.request.urlopen(the_url)
    except urllib.error.HTTPError as e:
        print("Invalid url!")
        print("Error Number: {}, Reason: {}".format(e.code, e.reason))
        return -1

    #load the file
    url_file = url_file.read()

    end = time.time() #end record time

    #get time_used
    time_used = end-start

    #get the size of the file and convert byte to kb
    size = sys.getsizeof(url_file)/1000

    #get the speed
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
    