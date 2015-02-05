#import Adder
#import unittest

#class TestAdder(unittest.TestCase):
 # """Test Adder.py's addNumbers() method"""
  #def testadd(self):
   # self.assertAlmostEqual(8,Adder.addNumbers(5,3),delta=1e-12)
    #self.assertEqual(8,Adder.addNumbers(5,3))
  

# Run the tests:
#if (__name__ == '__main__'):
 # unittest.main()
 
 import Function
 import unittest
 
 class TestFunction(unittest.TestCase):
  
  f = Function.Function
  
  def testFunction_dx_(self):
   x3 = f.xn(3)
   self.assertEqual(12.0, f.evaluate(x3.dx(), 2, 1))
   
  def testFunction_dy_(self):
   y3 = f.yn(3)
   self.assertEqual(48.0, f.evaluate(y3.dy(), 1, 4))
  
  def testFunction_xn_(self):
   x2 = f.xn(2)
   self.assertEqual(9.0, f.evaluate(x2, 3, 1))
  
  def testFunction_yn_(self):
   y2 = f.yn(2)
   self.assertEqual(25.0, f.evaluate(y2, 1, 5))
   
   
