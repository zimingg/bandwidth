import urllib.request
import time
import os
import sys

# def MeasureBandwidth2(url):
#     #set a timer
#     start = time.time()

#     #check and download url
#     try:
#         urllib.request.urlopen(url)
#     except:
#         return -1

#     #get time used
#     end = time.time()
#     time_used = end - start

#     #get size and convert it from byte to kb
#     size = os.path.getsize("./file")//1000

#     #get speed
#     speed = size//time_used

#     #remove downloaded file
#     os.remove("./file")

#     return speed

def MeasureBandwidth(url):
    #check if the input string is an url
    try:
        req = urllib.request.Request(url)
    except:
        print("invalid input!")
        return -1
    
    
    start = time.time() #start record time

    #open the url
    try:
        f = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("Invalid url!")
        print("Error Number: {}, Reason: {}".format(e.code, e.reason))
        return -1

    #load the file
    f = f.read()

    end = time.time() #end record time

    #get time_used
    time_used = end-start

    #get the size of the file and convert byte to kb
    size = sys.getsizeof(f)//1000

    #get the speed
    speed = size//time_used

    return speed


def main():
    #check if url is entered
    if len(sys.argv) <= 1: #nothing entered
        print("No url entered!")
    else:
        speed = MeasureBandwidth(sys.argv[1])
        if speed!=-1: 
            print("Bandwidth: {}kb/s ".format(int(speed)))
        


if __name__ == "__main__":
    main()
    