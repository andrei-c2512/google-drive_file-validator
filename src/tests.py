
from file_filtering import find_invalid_files
from google_api import *
from config_file_manager import ConfigFileManager

# DRIVE_ID = '1Rq8uetK6bnE6RrzMzf1QRBLUfRVSov8A'

# 
# Sa dau print la fisierele care vor fi sterse
# sa fac sa accepte argumente la linia de comanda
# optional , sa folosesc libraria de logging

def main():
    print("Nigger")
    manager = ConfigFileManager("config.config")
    manager.print_data()
     

if __name__ == "__main__":
    main()
