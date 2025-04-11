import os
import config
from config_file_management import ConfigFileReader

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
    def update_defaults(): 
        if os.path.exists(config.CONFIG_PATH):
            ConfigVars.update_by_all()
        else:
            ConfigVars.update_by_env()
    #
    @staticmethod
    def update_by_env():
        for key in ConfigVars.defaults:
            if key in os.environ:
                ConfigVars.defaults[key] = str(os.environ.get(key))
            #
        #
    #
    @staticmethod
    def update_by_all():
        reader = ConfigFileReader(config.CONFIG_PATH)

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

            




    
