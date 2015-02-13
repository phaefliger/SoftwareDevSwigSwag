import Function
import VarFactory
import Var
import BF
import MeshFactory
import unittest
import LinearTerm
 
class TestLinearTerm(unittest.TestCase):
  myFactory = VarFactory.VarFactory()
  var1 = myFactory.fieldVar("x")
  var2 = myFactory.fieldVar("y")
  var3 = myFactory.fieldVar("x^2")
  var4 = myFactory.fieldVar("y^3")
  ltMain = var1 + var2
  varFunctions = ({var1.ID(): Function.Function.xn(1), var2.ID(): Function.Function.yn(1), var3.ID(): Function.Function.xn(2), var4.ID(): Function.Function.yn(3)})

  #BEGIN TESTS
  
  def test_varIDs_(self):
   varID = (var1.ID(),var2.ID())
   self.assertEqual(varID, ltMain.varIDs())
    
  def test_displayString_(self):
   var1 = myFactory.fieldVar("x")
   var2 = myFactory.fieldVar("y")
   lt = var1 + var2
   self.assertEqual(lt.displayString(), 'x + y')
    
   
  def test_Rank_(self):
   global myFactory
   var1 = myFactory.fieldVar("Test")
   x2 = Function.Function.xn(2)
   y4 = Function.Function.yn(4)
   v = Function.Function.vectorize(x2, y4)
   lt1 = x2*var1
   lt2 = v*var1
   self.assertEqual(0, lt1.rank())
   self.assertEqual(1, lt2.rank())
   
  def test_termType_(self):
   var1 = myFactory.testVar("Test", HGRAD)
   f1 = Function.Function.xn(2)
   myLT = f1*var1
   bool = (myLT.termType() == Var.TEST)
   self.assertTrue(bool)
    
    
    #TESTING OVERLOADS
    
    #Add overloads
    
  def test_addLTLT_(self):
   ltTemp = var3 + var4
   ltTest = ltTemp + ltMain
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 80.0)
   
  def test_addLTV_(self):
   ltTest = ltMain + var3
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 16.0)
    
  def test_addVLT_(self):
   ltTest = var3 + ltMain
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 16.0)
      
  def test_addVV_(self):
   ltTest = var3 + var4
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 7.0)
      
      #Mul overloads
      
  def test_mulFV_(self):
   ltTest = Function.Function_xn(2) * var1
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 27.0)
      
  def test_mulVF_(self):
   ltTest =  var1 * Function.Function_xn(2) 
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 27.0)
  
  def test_mulDV_(self):
   ltTest = 2.0 * var1
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 6.0)
      
  def test_mulVD_(self):
   ltTest = var1 * 2.0
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3, 4), 6.0)
    
  def test_mulVecV_(self):
   vec = [1.0, 1.0]
   ltTest = vec * var1
   eval = ltTest.evaluate(varFunctions)
   x = eval.x()
   y = eval.y()
   self.assertEqual(x.evaluate(3, 4), 3.0)
   self.assertEqual(y.evaluate(3, 4), 4.0)
    
  def test_mulVVec_(self):
   vec = [1.0, 1.0]
   ltTest = var1 * vec
   eval = ltTest.evaluate(varFunctions)
   x = eval.x()
   y = eval.y()
   self.assertEqual(x.evaluate(3, 4), 3.0)
   self.assertEqual(y.evaluate(3, 4), 4.0) 
      
  def test_mulLTF_(self):
   ltTest = ltMain * Function.Function_xn(2)
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), 63.0)
      
     
    
    #Div overloads
    
  def test_divVW_(self):
   ltTest = var1 / 3.0
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), 1.0)
      
  def test_divVF_(self):
   ltTest = var1 / Function.Function_xn(1)
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), 1.0)
      
    
    #Neg and sub overloads
    
  def test_subVV_(self):
   ltTest = var1 - var2
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(4,3), 1.0)
      
  def test_negV_(self):
   ltTest = - var1
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), -3.0)
      
  def test_negLT_(self):
   ltTest = - ltMain
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), -7.0)
    
  def test_subLTV_(self):
   ltTest = ltMain - var1
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), 4.0)
    
  def test_subVLT_(self):
   ltTest = var1 - ltMain
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(3,4), -4.0)
    
  def test_subLTLT_(self):
   ltTemp = var3 + var4
   ltTest = ltTemp - ltMain
   eval = ltTest.evaluate(varFunctions)
   self.assertEqual(eval.evaluate(4,3), 36.0)
    
    
    
    
    
    
    
  
