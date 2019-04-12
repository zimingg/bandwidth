import unittest
from BandwidthMeasurer import BandwidthMeasurer

#unit test
class MyTestCase(unittest.TestCase):
    def test1(self):

        test1_url = "https://apod.nasa.gov/apod/imagess/1811/JupiterSwirls_JunoBrealey_3709.jjjjpg.wrong"
        test2_url = "dsdsdsdsd"
        test3_url = ""
        test4_url = "https://www.google.com/"
        test5_url = "https://apod.nasa.gov/apod/image/1811/JupiterSwirls_JunoBrealey_3709.jpg"

        print("RUN TEST NOW:")

        print("TEST1: [ {} ] 404 error, should raise Exception.".format(test1_url))
        self.assertRaises(Exception, BandwidthMeasurer().Measure,test1_url)

        print("TEST2: [ {} ] invalid input, should raise Exception.".format(test2_url))
        self.assertRaises(Exception, BandwidthMeasurer().Measure, test2_url)

        print("TEST3: [ {} ] nothing input, should raise Exception.".format(test3_url))
        self.assertRaises(Exception, BandwidthMeasurer().Measure, test3_url)

        print("TEST4: [ {} ] valid url with small file, shoud return an integer.".format(test4_url))
        self.assertTrue(isinstance(BandwidthMeasurer().Measure(test4_url),int),"It should be integer")

        print("TEST5: [ {} ] valid url with large file, shoud return an integer.".format(test5_url))
        self.assertTrue(isinstance(BandwidthMeasurer().Measure(test5_url),int),"It should be integer")
        
        print("ALL TESTS PASSED!")

def test():
    print("Unit Test:")
    MyTestCase().test1()

if __name__ == "__main__":
    #run unit test
    test()
    