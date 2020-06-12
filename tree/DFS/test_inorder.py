import unittest
import inorder

class Test_inorder(unittest.TestCase):
    def testcase(self):
        self.assertEqual(inorder.tree.h.p(), [4, 2, 5, 1, 6, 3, 7])


if __name__ == "__main__":
    unittest.main()