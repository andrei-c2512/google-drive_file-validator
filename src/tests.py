from file_filter import FileFilter
from google_api import *
from config_file_manager import ConfigFileManager
import csv
# DRIVE_ID = '1Rq8uetK6bnE6RrzMzf1QRBLUfRVSov8A'

# 
# Sa dau print la fisierele care vor fi sterse
# sa fac sa accepte argumente la linia de comanda
# optional , sa folosesc libraria de logging

CREDENTIALS_FOLDER="res"

TEST_RESULT_LIST=["FAILED","PASSED"]

logging.basicConfig(level=logging.INFO)


def indented_string(offset : int) -> str: 
    output_string : str = ""
    while offset != 0:
        # we add a tab
        output_string += '  '
        offset -= 1
    #

    return output_string
#

def index_string(index : int) -> str:
    output_string : str = ""
    if index < 0:
        logging.warning("The index of a test cannot be a negative number")
    elif index > 0:
        output_string += str(index) + "."
        
    return output_string
#

def test_result_string(test_output: str , expected_output : str) -> str:
    return TEST_RESULT_LIST[test_output == expected_output]
#

def show_test(test_input : str , test_output : str , expected_output : str,  index : int = 0, offset : int = 1) -> None:
    # we throw a warning if it's a negative number , and skip writing the index if it's ZERO
    output_string : str = indented_string(offset) + index_string(index) + " " 
    result : str = test_result_string(test_output , expected_output) 
    output_string += f"Input: {test_input} ---- {result}"

    logging.info(output_string)
#    

def show_test_detailed(test_input :str , test_output : str , expected : str , index : int , offset : int = 1) -> None: 
    output_string : str = indented_string(offset) + index_string(index) + " "
    
    result : str = test_result_string(test_output , expected)

    output_string += f"Input: {test_input} ---- {result}"
    if result == TEST_RESULT_LIST[False]:
        output_string += f"\nResult: {test_output}\n"
        output_string += f"Expected: {expected}"

    logging.info(output_string)
#
    
        
        
def basic_name_test(title : str , detailed : bool):
    logging.info(title)
    with open("tests/test1.csv", "r") as file:
        reader=csv.DictReader(file)
        index : int = 1
        for row in reader:
            filter = FileFilter(row["input"] , 10000 , "123121123")
            test_result = str(filter.is_valid(log_errors = False))
                           
            if detailed:
                show_test_detailed(row["input"], test_result , row["expected"] , index)
            else:
                show_test(row["input"], test_result , row["expected"] , index)
            index +=1
        #
    #
#

def main():
    manager = ConfigFileManager(f"{CREDENTIALS_FOLDER}/config.config")
    manager.print_data()
    
    manager.set_var("PATTERN", "2024-12-13")
    basic_name_test("Test 1" , True)
#

if __name__ == "__main__":
    main()
#
