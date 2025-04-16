import unittest
import numpy as np
from mainclass import TestScoreAnalysis
from test.TestUtils import TestUtils
import pandas as pd


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.student_ids = [101, 102, 103, 104, 105]
        self.test_scores = [60, 70, 40, 90, 80]
        self.test_analysis = TestScoreAnalysis(self.student_ids, self.test_scores)

    def test_fancy_indexing(self):
        test_obj = TestUtils()
        try:
            """Test if fancy indexing works correctly"""
            obj = self.test_analysis.fancy_indexing()
            expected_output = np.array([60, 40, 80], dtype=np.float32)
            
            if np.array_equal(obj, expected_output):
                test_obj.yakshaAssert("TestFancyIndexing", True, "functional")
                print("TestFancyIndexing = Passed")
            else:
                test_obj.yakshaAssert("TestFancyIndexing", False, "functional")
                print("TestFancyIndexing = Failed")
        except:
            
            test_obj.yakshaAssert("TestFancyIndexing", False, "functional")
            print("TestFancyIndexing = Failed")
                
    def test_boolean_indexing(self):
        """Test if boolean indexing works correctly"""
        test_obj = TestUtils()
        try:
            obj = self.test_analysis.boolean_indexing()
            expected_output = np.array([60, 70, 90, 80], dtype=np.float32)
            test_obj = TestUtils()
            if np.array_equal(obj, expected_output):
                test_obj.yakshaAssert("TestBooleanIndexing", True, "functional")
                print("TestBooleanIndexing = Passed")
            else:
                test_obj.yakshaAssert("TestBooleanIndexing", False, "functional")
                print("TestBooleanIndexing = Failed")
        except:
            test_obj.yakshaAssert("TestBooleanIndexing", False, "functional")
            print("TestBooleanIndexing = Failed")
    
    def test_mean_score(self):
        """Test if mean score is calculated correctly"""
        test_obj = TestUtils()
        try:
            obj = self.test_analysis.mean_score()
            expected_output = np.mean(self.test_scores)
            test_obj = TestUtils()
            if np.isclose(obj, expected_output):
                test_obj.yakshaAssert("TestMeanScore", True, "functional")
                print("TestMeanScore = Passed")
            else:
                test_obj.yakshaAssert("TestMeanScore", False, "functional")
                print("TestMeanScore = Failed")
        except:
            test_obj.yakshaAssert("TestMeanScore", False, "functional")
            print("TestMeanScore = Failed")

    def test_median_score(self):
        """Test if median score is calculated correctly"""
        test_obj = TestUtils()
        try:
            obj = self.test_analysis.median_score()
            expected_output = np.median(self.test_scores)
            test_obj = TestUtils()
            if np.isclose(obj, expected_output):
                test_obj.yakshaAssert("TestMedianScore", True, "functional")
                print("TestMedianScore = Passed")
            else:
                test_obj.yakshaAssert("TestMedianScore", False, "functional")
                print("TestMedianScore = Failed")
        except:
            test_obj.yakshaAssert("TestMedianScore", False, "functional")
            print("TestMedianScore = Failed")

    def test_standard_deviation(self):
        """Test if standard deviation is calculated correctly"""
        test_obj = TestUtils()
        try:
            obj = self.test_analysis.standard_deviation()
            expected_output = np.std(self.test_scores)
            test_obj = TestUtils()
            if np.isclose(obj, expected_output):
                test_obj.yakshaAssert("TestStandardDeviation", True, "functional")
                print("TestStandardDeviation = Passed")
            else:
                test_obj.yakshaAssert("TestStandardDeviation", False, "functional")
                print("TestStandardDeviation = Failed")
        except:
            test_obj.yakshaAssert("TestStandardDeviation", False, "functional")
            print("TestStandardDeviation = Failed")