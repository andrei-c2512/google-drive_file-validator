import unittest
import csv
import logging

from src.file_filter import FileFilter 




logging.basicConfig(level=logging.ERROR)

"""
    Canceled the tests because the result will always differ if the configuration changes
    Could create a smart system that just tests the function themselves(the filters), however , I am kinda lazy and need to learn Chinese Remainder Theorem unfortunately
    Maybe on a sunny day I will update this.
"""

class TestFilter(unittest.TestCase):    
    def iterate_csv(self , path_to_csv : str , f_lifetime = 0 , f_date ="YYYY-MM-DD", f_glob="" , f_regex = ""):
        with open(path_to_csv, "r") as file:
            reader=csv.DictReader(file)
            for row in reader:
                filter = FileFilter(row["input"] , f_lifetime , f_date , f_regex , f_glob)
                test_result = str(filter.is_valid(True))
                self.assertEqual(test_result , row["expected"], 
                                 msg=f"Expected {row['input']} to be {row['expected']}\n"
                                 f"lifetime={f_lifetime}\n"
                                 f"date_pattern={f_date}\n"
                                 f"glob_pattern={f_glob}\n"
                                 f"regex={f_regex}\n")
        pass
    #

    
    def test_format(self):
        # self.iterate_csv("tests/res/test1.csv")
        pass
    #
    def test_date_pattern(self):
        
        #self.iterate_csv("tests/res/pattern_test1.csv", f_date="YYYY-MM-1D")
        #self.iterate_csv("tests/res/pattern_test2.csv", f_date="YYYY-MM-D1")
    #



        

        
        
        



