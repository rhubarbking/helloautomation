import unittest
import os
import time
import datetime

from setests import HTMLTestRunner
from setests.searchtests import SearchTest
from homepagetests import HomePageTest



# get the directory to save the html report
dir = os.getcwd()



# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)



# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# fetch time and convert to time stamp
datetimestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H.%M.%S')

# open the html report file
outfile = open(dir + "/SmokeTestReport_" + datetimestamp + ".html", "w")



# configure the HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='Test Report',
    description='Smoke Tests'
)



# run the suite
runner.run(smoke_tests)