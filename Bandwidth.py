import urllib.request
import time
import os
import sys

def MeasureBandwidth(url):
    #set a timer
    start = time.time()

    #check and download url
    try:
        urllib.request.urlretrieve(url, "./file")
    except:
        return -1

    #get time used
    end = time.time()
    time_used = end - start

    #get size and convert it from byte to kb
    size = os.path.getsize("./file")//1000

    #get speed
    speed = size//time_used

    #remove downloaded file
    os.remove("./file")

    return speed

def main():
    #check if url is entered
    if len(sys.argv) <= 1: #nothing entered
        print("No url entered!")
    else:
        speed = MeasureBandwidth(sys.argv[1])
        if speed!=-1: 
            print("Bandwidth: {}kb/s ".format(int(speed)))
        else: #invalid url
            print("invalid url")


if __name__ == "__main__":
    main()

    
