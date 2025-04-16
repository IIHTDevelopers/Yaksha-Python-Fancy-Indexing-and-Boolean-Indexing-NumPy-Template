import unittest
import numpy as np
from mainclass import TestScoreAnalysis
from test.TestUtils import TestUtils
import pandas as pd

class BoundaryTest(unittest.TestCase):
    def test_single_student(self):
        """Test system with only one student"""
        test_obj = TestUtils()
        try:
            single_student = TestScoreAnalysis([101], [60])
            obj = single_student.mean_score()
            expected_output = 60
            
            if np.isclose(obj, expected_output):
                test_obj.yakshaAssert("TestSingleStudent", True, "boundary")
                print("TestSingleStudent = Passed")
            else:
                test_obj.yakshaAssert("TestSingleStudent", False, "boundary")
                print("TestSingleStudent = Failed")
        except:
            test_obj.yakshaAssert("TestSingleStudent", False, "boundary")
            print("TestSingleStudent = Failed")
                
                
    def test_two_students(self):
        """Test system with two students"""
        test_obj = TestUtils()
        try:
            two_students = TestScoreAnalysis([101, 102], [60, 70])
            obj = two_students.mean_score()
            expected_output = 65
            
            if np.isclose(obj, expected_output):
                test_obj.yakshaAssert("TestTwoStudents", True, "boundary")
                print("TestTwoStudents = Passed")
            else:
                test_obj.yakshaAssert("TestTwoStudents", False, "boundary")
                print("TestTwoStudents = Failed")
        except:
            test_obj.yakshaAssert("TestTwoStudents", False, "boundary")
            print("TestTwoStudents = Failed")
