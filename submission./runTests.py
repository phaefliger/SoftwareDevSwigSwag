#from TestAdder import * #this syntax imports whatever is defined in TestAdder into the current namespace
#from TestTimes import *
#import unittest

#testSuite = unittest.makeSuite(TestAdder)
#testSuite.addTest(unittest.makeSuite(TestTimes))

#testRunner = unittest.TextTestRunner()
#testRunner.run(testSuite)

from TestFunction import *
from TestLinearTerm import *
from TestSpatialFilter import *
from TestRHS import *
import unittest

testSuite = unittest.makeSuite(TestFunction)
testSuite.addTest(unittest.makeSuite(TestLinearTerm))
testSuite.addTest(unittest.makeSuite(TestSpatialFilter))
testSuite.addTest(unittest.makeSuite(TestRHS))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
