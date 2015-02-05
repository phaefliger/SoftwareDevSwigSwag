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
        xy = x & y
        self.assertEqual(xy, sf.allSpace())
