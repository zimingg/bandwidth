import sys
from MyTest import MyTestCase
from Measure import MyMeasure
import urllib.request

def main():
    #check if url is entered
    if len(sys.argv) <= 1: #nothing entered
        print("No url entered!")
    else:
        try:
            speed = MyMeasure().MeasureBandwidth(sys.argv[1])
            print("Bandwidth: {}kb/s ".format(speed))
        except ValueError:
            print("Unknown url type")
        except urllib.error.HTTPError as e:
            print("URL Error! Error Number: {}, Reason: {} ".format(e.code, e.reason))

if __name__ == "__main__":
    main()
    print("---------------------------")
    #run unit test
    print("Unit Test:")
    MyTestCase().test1()
    