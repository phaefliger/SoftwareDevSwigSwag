import RHS
import unittest

class TestRHS(unittest.TestCase):
    
    rhs = RHS.RHS

    # constructors
    def test_RHS_(self):
        self.assertEqual(rhs.RHS(), rhs.RHS(false))
        
