from google_api import *
import logging
import os
import datetime
import fnmatch
import re


class FileFilter:
    def __init__(self , file_name :str , lifetime : int , date_pattern : str , regex : str = "" , glob_pattern : str = ""):
        self.file_name = file_name
        self.lifetime = lifetime
        self.date_pattern = date_pattern
        self.glob_pattern = glob_pattern
        self.file_metadata : list[str] = []
        self.date_fields : list[str] = []
        self.time_fields : list[str] = []
        self.time : datetime.time 
        self.name : str = ""
        self.error_message : str = ""
        self.regex = regex


        self.tests = [ self.pattern_filter, self.value_filter]
    #
    def add_error(self, message : str):
        if len(self.error_message) == 0:
            self.error_message += message 
        else:
            self.error_message += "\n" + message
        return 
    #
    def pattern_filter(self) -> bool:
        error_message : str = f"File {self.file_name} was skipped because of invalid pattern: A valid pattern is: "
        error_message += "{}"
        file_metadata = self.file_name.split("_", 2)
        if len(file_metadata) < 3:
            self.add_error(error_message.format("<date>_<time>_<name>"))
            return False
        self.string = file_metadata[2]
        
        self.date_fields = file_metadata[0].split("-", 2)
        if len(self.date_fields) < 3:
            self.add_error(error_message.format("YYYY-MM-DD"))
            return False
        # 
        self.time_fields = file_metadata[1].split("-", 2)
        if len(self.date_fields) < 3:
            self.add_error(error_message.format("HH-MM-SS"))
            return False
        #

        return True
    #
    def date_time_test(self , begin : int , end : int , value : int , field_name : str) -> bool:
        if (value in range(begin , end)) == False:
            self.add_error(f"The {field_name} field has an invalid value")
            return False
        #
        return True
    #

    @staticmethod 
    def date_field_match( field : str , val : str) -> bool:
       if len(field) != len(val):
           return False

       for i in range(0, len(field)):
           if field[i].isnumeric() and field[i] != val[i]:
               return False
           #
        #
       return True
    #
    def value_filter(self) -> bool:
        # TO DO: force prerequisite test 
        try:
            hours : int = int(self.time_fields[0])
            minutes : int = int(self.time_fields[1])
            seconds : int = int(self.time_fields[2])
        
            year : int = int(self.date_fields[0])
            month : int = int(self.date_fields[1])
            day : int = int(self.date_fields[2])

            passed : bool = self.date_time_test(0 , 24, hours , "hours") and \
                    self.date_time_test(0 , 60, minutes, "minutes") and      \
                    self.date_time_test(0, 60 , seconds, "seconds") and      \
                    self.date_time_test(1 , 13, month , "months") and \
                    self.date_time_test(0 , 32 , day,  "days")

            self.time = datetime.time(hours , minutes , seconds)
            self.date = datetime.date(year , month , day)
        except ValueError as e:
            self.add_error(f"File {self.file_name} was skipped:" + str(e))
            return False
        #
        return passed
    #
    # warning: the date filter will be run inside this function , meaning that , if it respects the date pattern, even if the file is too old
    # it will still not be deleted
    def lifetime_filter(self) -> bool:
        if self.lifetime == 0:
            return True
        if self.date_filter() == True:
            return True
        
        current_date: datetime.datetime = datetime.datetime.now()

        file_lifetime: int = (current_date.date() - self.date).days
        return file_lifetime < self.lifetime
    #
    def glob_filter(self) -> bool:
        if len(self.glob_pattern) == 0:
            return True
        else:
            return fnmatch.fnmatch(self.file_name, self.glob_pattern)
    #

    def date_filter(self) -> bool:
        date_pattern_fields = self.date_pattern.split('-', 2)

        passed : bool = True
        for i in range(0 , 3):
            passed = (passed and self.date_field_match(date_pattern_fields[i], self.date_fields[i]))
       
        # if it passed the test , then it needs to be skipped
        return passed == False
    #
    def regex_filter(self) -> bool:
        if len(self.regex) == 0:
            return True
        else:
            return re.fullmatch(self.regex , self.file_name) != None
    #
    def is_valid(self, log_errors : bool = True) -> bool:
        result  = self.glob_filter() and self.pattern_filter() and self.value_filter() \
                and self.date_filter() and self.lifetime_filter() and self.glob_filter() and self.regex_filter()

        if log_errors == True and len(self.error_message) != 0:
            logging.error(self.error_message)
        #
        if log_errors == True and result == False and len(self.error_message) == 0:
            logging.error(f"File '{self.error_message}' was skipped due to unknown reasons")
        return result
    #
#


def find_invalid_files(file_list , lifetime : int, pattern : str):
    invalid_file_list = []

    for file_item in file_list:
        try:
            # splits the name into two (name and extension), we store the name
            file_name = os.path.splitext(file_item["name"])[0]
            filter = FileFilter(file_name , lifetime , pattern)
            if filter.is_valid():
                invalid_file_list.append(file_item)

        except Exception as e:
            logging.error(
                f"There was an exception: {e}. The file with the name '{file_item['name']}' was ignored"
            )

    return invalid_file_list
#

def validate_a( args):
    validate(args.driveId , args.folderId ,
             int(args.lifetime) , args.pattern , 
             args.glob , args.regex, 
             bool(args.force))
    return 
#
def validate( drive_id : str, folder_id : str , lifetime : int , pattern : str , glob : str , regex : str, force : bool):
    # error checks
    if drive_id == "NULL":
        logging.error("Please provide a valid drive id , either directly by argument , or modify the configuration file")
        return
    if lifetime < 0:
        logging.error("You can't have negative values as a lifetime value")
        return
    
    # TO DO: validate the pattern    

    # the actual validation 
    try:
        service = build_service()
        items = get_drive_files(service, drive_id , folder_id)
        for item in items:
            print_params(item)

        if not items:
            logging.info("No files found.")
            return

        invalid_file_list = find_invalid_files(items ,  lifetime ,pattern)

        if len(invalid_file_list) == 0:
            print("No files are going to be deleted")
            return
        else:
            print_drive_files(invalid_file_list , ['name'])
        user_input = "joe"
        while (user_input[0] == "y" or user_input[0] == "n") == False:
            user_input = input("The files listed above are going to be deleted. Are you sure? [y/n]: ")
        #
        if user_input == "y":
            print(f"Deleting {len(invalid_file_list)} files")
            for item in invalid_file_list:
                logging.info(f"Deleting file {item['name']}")
                service.file().delete(fileId=f"{item['id']}", supportsAllDrives=True).execute()
        else:
            print("Deletion canceled. Exiting the program...")

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        logging.error(f"An error occurred: {error}")
#
