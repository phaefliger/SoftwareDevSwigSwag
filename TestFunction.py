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
   self.assertAlmostEqual(16.0, f.evaluate(v.x(), 4, 1), delta=1e-12)
   
  def test_y_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertAlmostEqual(81.0, f.evaluate(v.x(), 1, 3), delta=1e-12)
  
  def test_dx_(self):
   x3 = f.xn(3)
   self.assertAlmostEqual(12.0, f.evaluate(x3.dx(), 2, 1), delta=1e-12)
   
  def test_dy_(self):
   y3 = f.yn(3)
   self.assertAlmostEqual(48.0, f.evaluate(y3.dy(), 1, 4), delta=1e-12)
  
  def test_div_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertAlmostEqual(40.0, f.evaluate(v.div(), 4, 2), delta=1e-12)
   
  def test_grad_(self):
   
   
  def test_rank_(self):
   x2 = f.xn(2)
   y4 = f.yn(4)
   v = f.vectorize(x2, y4)
   self.assertEqual(0, x2.rank())
   self.assertEqual(1, v.rank())
   
  def test_l2norm_(self):
   
   
  def test_displayString_(self):
   
   
  def test_evaluate_(self):
   x2 = f.xn(2)
   y3 = f.yn(3)
   self.assertAlmostEqual(31.0, f.evaluate(x2+y3, 2, 3), delta=1e-12)
   
  def test_composedFunction_(self):
   
   
  def test_constant_(self):
   
   
  def test_vectorize_(self):
   
   
  def test_normal_(self):
   
   
  def test_solution(self):
   
   
  
  def test_xn_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(9.0, f.evaluate(x2, 3, 1), delta=1e-12)
  
  def test_yn_(self):
   y2 = f.yn(2)
   self.assertAlmostEqual(25.0, f.evaluate(y2, 1, 5), delta=1e-12)
   
  def test_mult2f_(self):
   x2 = f.xn(2)
   y2 = f.yn(2)
   self.assertAlmostEqual(36.0, f.evaluate(x2*y2, 2, 3), delta=1e-12)
   
  def test_divide2f_(self):
   x2 = f.xn(2)
   y2 = f.yn(2)
   self.assertAlmostEqual(4.0, f.evaluate(x2/y2, 4, 2), delta=1e-12)
   
  def test_dividefd_(self):
   x2 = f.xn(2)
   self.assertAlmostEqual(8.0, f.evaluate(x2/2, 4, 1), delta=1e-12)
   
