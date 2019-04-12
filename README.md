# MeasureBandwidth

  This is a Python program that measures your internet bandwidth. The project accept a URL as a command-line argument and     print the kilobytes per second that it takes to fetch that URL.

## Project Details
* BandwidthMeasurer.py

  In BandwidthMeasurer class, I implemented a function Measure which take an URL as input and return an integer.

  1. If the input URL is invalid or the URL has a HTTP ERROR, raise Exception.

  2. Use the valid URL to get response. We do not store it but count the size while reading through it.

  3. Get the speed by size / duration, and return.


* MyTest.py

  * Include unit test for this program. Details below.

* BandwidthMeasureCli.py

  This is the main function to measure the bandwidth.
  
  1. Get command-line argument, if no url entered, stop.
  
  2. Call Measure(), if no exception raised, print the bandwidth, or catch Exceptions and print error reason.
  

## Getting Started

  These instructions will get you a copy of the project up and running on your local machine for development and testing       purposes. 

### Prerequisites

  Python3


### Run the program

  1. Get into the folder through terminal
  2. run this line in terminal
  ```console
    $ python3 BandwidthMeasureCli.py (YOUR URL)
  ```



## Running the tests
  1. Get into the folder through terminal
  2. run this line in terminal
  ```console
    $ python3 MyTest.py 
  ```
  

### Details about tests
  There are 5 tests:

  * Test1: Check if it raise an exception when have Http Error.

  * Test2: Check if it raise an exception when the input is not a url.

  * Test3: Check if it raise an exception when input is empty.

  * Test4: Check if it has integer type return when enter an url with small size file.

  * Test5: Check if it has integer type return when enter an url with large size file.


## Authors

  * **Ziming Guo** 


