from rotten_oranges import SolutionOrange
import unittest

class TestRottenOranges(unittest.TestCase):
    def setUp(self) -> None:
        self.objOrange = SolutionOrange()
        return super().setUp()
    
    def test_code(self):
        l = l =[[0,1,2],[0,1,2],[2,1,1]]
        self.assertEqual(self.objOrange.orangesRotting(l), 1)
    
    @unittest.expectedFailure
    def test_failure(self):
        l = l =[[0,1,2],[0,1,2],[2,1,1]]
        self.assertEqual(self.objOrange.orangesRotting(l), 2)
    
    def tearDown(self) -> None:
        print("tearing down variables")
        return super().tearDown()


# if __name__ == "__main__":
#     unittest.main()