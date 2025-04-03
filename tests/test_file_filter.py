import unittest
import csv
import logging

from src.file_filter import FileFilter

logging.basicConfig(level=logging.ERROR)

class TestFilter(unittest.TestCase):    
    def iterate_csv(self , path_to_csv : str , f_lifetime = 0 , f_date ="YYYY-MM-DD", f_glob="" , f_regex = ""):
        with open(path_to_csv, "r") as file:
            reader=csv.DictReader(file)
            for row in reader:
                filter = FileFilter(row["input"] , f_lifetime , f_date , f_regex , f_glob)
                test_result = str(filter.is_valid(log_errors = False))
                self.assertEqual(test_result , row["expected"], 
                                 msg=f"Expected {row['input']} to be {row['expected']}\n"
                                 f"lifetime={f_lifetime}\n"
                                 f"date_pattern={f_date}\n"
                                 f"glob_pattern={f_glob}\n"
                                 f"regex={f_regex}\n")
        pass



    def test_format(self):
        self.iterate_csv("tests/res/test1.csv")
    #
    def test_date_pattern(self):
        self.iterate_csv("tests/res/pattern_test1.csv", f_date="YYYY-MM-1D")
        self.iterate_csv("tests/res/pattern_test2.csv", f_date="YYYY-MM-D1")
    #



        

        
        
        



