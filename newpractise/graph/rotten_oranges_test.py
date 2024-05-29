from rotten_oranges import SolutionOrange
import unittest

class TestRottenOranges(unittest.TestCase):
    def setUp(self) -> None:
        self.objOrange = SolutionOrange()
        return super().setUp()
    
    def test_code(self):
        l = l =[[0,1,2],[0,1,2],[2,1,1]]
        self.assertEqual(self.objOrange.orangesRotting(l), 2)
