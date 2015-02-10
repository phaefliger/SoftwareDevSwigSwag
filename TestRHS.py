import RHS
import unittest
import LinearTerm

class TestRHS(unittest.TestCase):
    
    rhs = RHS.RHS

    # constructors
    def test_RHS_(self):
        self.assertEqual(rhs.RHS(), rhs.RHS())
        
    # --- not sure how RHS works, need more info to write tests for nonZeroRHS and addTerm
    
    def test_linearTerm_(self):
        r = rhs.RHS()
        lt = r.linearTerm()
        # --- need LinearTerm to be working so I know how to test it. will want to change the linearTerm and compare it to the RHS
        self.assertEqual(r, lt)
    
    def test_linearTermCopy(self):
        r = rhs.RHS()
        lt = r.linearTermCopy()
        # --- need LinearTerm to be working so I know how to test it. will want to change the linearTerm and compare it to the RHS
        self.assertNotEqual(r, lt)
    
