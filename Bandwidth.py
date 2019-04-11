import urllib.request
import time as timer
import os
import sys
import unittest


def MeasureBandwidth(url):
    # check if input is a valid url
    try:
        request = urllib.request.Request(url)
    except:
        print("Exception: Input is not a valid url!")
        raise Exception
       
    start = timer.time() 

    # check if there is any error loading the url
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        print("Exception: URL Error! Error Number: {}, Reason: {} ".format(e.code, e.reason))
        raise Exception

    #fully load the file
    content = response.read()

    end = timer.time() 

    time_used = end-start
    #convert byte to kb
    size = sys.getsizeof(content)/1000
    speed = size/time_used

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
       
#unit test
class MyTestCase(unittest.TestCase):
    def test1(self):
        print("RUN TEST NOW:")
        print("TEST1: 404 error, should raise Exception.")
        self.assertRaises(Exception, MeasureBandwidth,"https://apod.nasa.gov/apod/imagess/1811/JupiterSwirls_JunoBrealey_3709.jjjjpg")
        print("TEST2: invalid input, should raise Exception.")
        self.assertRaises(Exception, MeasureBandwidth,"ssdsds")
        print("TEST3: valid url, shoud return an integer.")
        self.assertTrue(isinstance(MeasureBandwidth("https://www.google.com/"),int),"It should be integer")
        print("TEST4: valid url with large file, shoud return an integer.")
        self.assertTrue(isinstance(MeasureBandwidth("https://apod.nasa.gov/apod/image/1811/JupiterSwirls_JunoBrealey_3709.jpg"),int),"It should be integer")
        print("ALL TEST PASSED!")



if __name__ == "__main__":
    main()
    print("---------------------------")
    #run unit test
    print("Unit Test:")
    test = MyTestCase()
    test.test1()
    