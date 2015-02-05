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
