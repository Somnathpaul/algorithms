import unittest
import postorder

class Test_postorder(unittest.TestCase):
    def testcase(self):
        self.assertEqual(postorder.tree.helper.print(), [4, 5, 2, 6, 7, 3, 1])

if __name__ == "__main__":
    unittest.main()