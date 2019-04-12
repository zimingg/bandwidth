import sys
from MyTest import MyTestCase
from Measure import BandwidthMeasurer
import urllib.request

def main():
    #check if url is entered
    if len(sys.argv) <= 1: #nothing entered
        print("No url entered!")
    else:
        try:
            speed = BandwidthMeasurer().Measure(sys.argv[1])
            print("Bandwidth: {}kb/s ".format(speed))
        except ValueError:
            print("Unknown url type")
        except urllib.error.HTTPError as e:
            print("URL Error! Error Number: {}, Reason: {} ".format(e.code, e.reason))
        except Exception as e:
            print("unexpect error occurred")

def test():
    print("Unit Test:")
    MyTestCase().test1()

if __name__ == "__main__":
    main()
    print("---------------------------")
    #run unit test
    test()
    
    