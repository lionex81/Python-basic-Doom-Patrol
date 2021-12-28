import unittest
import functions_for_testing as fft

class FunctionsTest(unittest.TestCase):
    def test_div(self):
        self.assertEqual(fft.div(10, 5), 2)
        self.assertNotEqual(fft.div(40, 4), 9)
        self.assertEqual(fft.div(100, 25), 4)
        self.assertEqual(fft.div(444, 222), 2)