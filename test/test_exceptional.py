import unittest
from mainclass import TestScoreAnalysis
from test.TestUtils import TestUtils
import numpy as np
import pandas as pd

class ExceptionalTests(unittest.TestCase):
    def test_invalid_data_type(self):
        """Test if invalid data type (e.g., strings) raises error"""
        test_obj = TestUtils()
        try:
            invalid_data = TestScoreAnalysis([101], ["invalid_data"])  # Invalid score data
            invalid_data.fancy_indexing()
            test_obj.yakshaAssert("TestInvalidDataType", False, "exceptional")
            print("TestInvalidDataType = Failed")
        except ValueError as e:
            if "could not convert string to float" in str(e):
                test_obj.yakshaAssert("TestInvalidDataType", True, "exceptional")
                print("TestInvalidDataType = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidDataType", False, "exceptional")
                print("TestInvalidDataType = Failed")
