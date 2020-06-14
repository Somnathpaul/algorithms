import unittest
import preorder

class Test(unittest.TestCase):
    def testcase(self):
        self.assertEqual(preorder.tree.helper.print(), [1, 2, 4, 5, 3, 6, 7])

if __name__ == "__main__":
    unittest.main()
