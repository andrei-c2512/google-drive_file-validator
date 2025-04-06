import config
import config_vars
import os

class ConfigSanityChecker:
    @staticmethod
    def create_default():
         file_vars : dict[str, str] = config_vars.ConfigVars.defaults
        
         with open(config.CONFIG_PATH, "w") as file:
             file_contents = ""
             for key , value in file_vars.items():
                 file_contents += key + "=" + value + "\n"
             file.write(file_contents)
            
         return
    #
    @staticmethod
    def run() -> None:
        if os.path.exists(config.CONFIG_PATH):
            ConfigSanityChecker.create_default()
        else:
            # TO DO: make it run a validity check on the .sh file
            pass
        return
#
