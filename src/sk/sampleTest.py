import unittest
import sample

class SampleTest(unittest.TestCase):

    def test_add(self):
        actual = sample.add(10, 20)
        self.assertEqual(actual, 30)

if __name__ == '__main__':
    unittest.main()