import program
import unittest

class Test_program(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(program.reverse(-321), -123)
    def testcase2(self):
        self.assertEqual(program.reverse(120), 21)
    def testcase3(self):
        self.assertEqual(program.reverse(0), 0)


if __name__ == '__main__': 
    unittest.main() 