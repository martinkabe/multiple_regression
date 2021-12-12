"""
Test module pro tridu MatrixCalc
"""
import unittest
from MatrixCalc import MatrixCustom

class TestMatrixCalc(unittest.TestCase):
    """
    Test pro nejakou konkretni funkci
    """
    def test_power_function(self):
        self.assertEqual(MatrixCustom.power_function(5, 4), 9)


if __name__ == '__main__':
    unittest.main()