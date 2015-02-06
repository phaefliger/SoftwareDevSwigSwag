import SpatialFilter
import unittest

class TestSpatialFilter(unittest.TestCase):

    sf = SpatialFilter.SpatialFilter

    # MatchesPoint Test
    def testFunc_matchesPoint_(self):
        x = sf.matchingX(2.0)
        y = sf.matchingY(4.0)
        xy = x | y
        self.assertEqual(True, xy.matchesPoint(2.0, 4.0))

    # allSpace test
    def testFunc_allSpace(self):
        x = sf.matchingX(1.0)
        y = sf.negatedFilter(x)
        xy = x | y
        self.assertEqual(xy, sf.allSpace())

    # unionFilter
    def testFunc_unionFilter(self):
        x = sf.matchingX(36.0)
        y = sf.matchingY(64.0)
        xy = sf.unionFilter(x, y)
        self.assertEqual(True, xy.matchesPoint(36.0, 64.0)
        
    # intersectionFilter
    def testFunc_intersectionFilter(self):
        x = sf.greaterThanX(1.0)
        y = sf.allSpace()
        xy = sf.intersectionFilter(x, y)
        self.assertEqual(xy, x)
        
    # negatedFilter
    def testFunc_negatedFilter(self):
        x = sf.matchingX(1.0)
        y = sf.negatedFilter(x)
        xy = x & y
        self.assertEqual(xy, sf.negatedFilter(sf.allSpace()))

    # matchingX
    def testFunc_matchingX(self):
        x = sf.matchingX(8.0)
        self.assertEqual(True, x.matchesPoint(8.0, 24.0))

     # matchingY
    def testFunc_matchingY(self):
        y = sf.matchingY(8.0)
        self.assertEqual(True, y.matchesPoint(24.0, 8.0))

    # lessThanX
    def testFunc_lessThanX(self):
        x = sf.lessThanX(8.0)
        self.assertEqual(False, x.matchesPoint(8.1, 24.0))
    
    # lessThanY
    def testFunc_lessThanY(self):
        x = sf.lessThanY(8.0)
        self.assertEqual(False, x.matchesPoint(24.0, 8.1))
    
    # greaterThanX
    def testFunc_greaterThanX(self):
        x = sf.greaterThanX(8.0)
        self.assertEqual(True, x.matchesPoint(8.1, 24.0))
    
    # greaterThanY
    def testFunc_greaterThanY(self):
        x = sf.greaterThanY(8.0)
        self.assertEqual(True, x.matchesPoint(24.0, 8.1))
    
