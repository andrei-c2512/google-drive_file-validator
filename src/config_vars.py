import os
import logging
from . import globals
from .config_file_management import ConfigFileReader

class ConfigVars:
    defaults : dict[str, str] = {}
    defaults.update( { "DATE_PATTERN" : "YYYY-MM-DD"})
    defaults.update({"REGEX" : ""})
    defaults.update({"LIFETIME":"0"})
    defaults.update({"IGNORE_LIST":""})
    defaults.update({"GLOB":""}) 
    defaults.update({"FOLDER_ID":""})
    defaults.update({"DRIVE_ID":""})

    @staticmethod
    def run():
        reader = ConfigFileReader(globals.CONFIG_PATH)
        for key in ConfigVars.defaults:
            new_val : str = ""
            if key in os.environ:
                new_val = str(os.environ.get(key))
            else:
                new_val = reader.get_var(key)
            ConfigVars.defaults[key] = new_val
        #
    #
    @staticmethod
    def print_defaults() -> None:
        output_str : str = ""
        for key , value in ConfigVars.defaults.items():
            output_str += key + "=" + value +'\n'
        #
    #

            




    
