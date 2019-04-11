# MeasureBandwidth

This is a Python program that measures your internet bandwidth. The project accept a URL as a command-line argument and print the kilobytes per second that it takes to fetch that URL.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
Python3


### Run the program

1. Get into the folder through terminal
2. run "python3 Main.py (YOUR URL)"



## Running the tests

It will automatically run the test after measure the url you input. 

You can cancle it by comment out "MyTestCase().test1()" in Main.py

### Details about tests
There are 5 tests:

* Test1: Check if it raise an exception when have Http Error.

* Test2: Check if it raise an exception when the input is not a url.

* Test3: Check if it raise an exception when input is empty.

* Test4: Check if it has integer type return when enter an url with small size file.

* Test5: Check if it has integer type return when enter an url with large size file.


## Authors

* **Ziming Guo** 


