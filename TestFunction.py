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
  
  def test_x_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertEqual(16.0, f.evaluate(v.x(), 4, 1))
   
  def test_y_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertEqual(81.0, f.evaluate(v.x(), 1, 3))
  
  def test_dx_(self):
   x3 = f.xn(3)
   self.assertEqual(12.0, f.evaluate(x3.dx(), 2, 1))
   
  def test_dy_(self):
   y3 = f.yn(3)
   self.assertEqual(48.0, f.evaluate(y3.dy(), 1, 4))
  
  def test_xn_(self):
   x2 = f.xn(2)
   self.assertEqual(9.0, f.evaluate(x2, 3, 1))
  
  def test_yn_(self):
   y2 = f.yn(2)
   self.assertEqual(25.0, f.evaluate(y2, 1, 5))
   
   
