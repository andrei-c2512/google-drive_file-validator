import logging
# this class manager a .config file. It works in a simple way: since everything is stored in a key value pair(in the file)
# I do that as well here. If you modify a file variable here , it will modify it in the file
class ConfigFileManager:
    def __init__(self , path):
        self.path : str = path

        # TO DO: check if the file *actually* exists

        self.file_vars : dict[str, str] = {}
        with open(path , 'r') as file:
            file.seek(0)
            for line in file:
                line = line.lstrip()
                if len(line) != 0 and line[0] == '#':
                    continue 
                parts = line.split(':', 1)
                if len(parts) != 2:
                    continue

                parts[1] = parts[1].lstrip()

                # we remove the end of line character if it has one , because it is annoying
                if len(parts[1]) != 0 and parts[1][len(parts[1]) -1] == '\n':
                    parts[1] = parts[1][:-1]
                
                self.file_vars.update( { parts[0] : parts[1]})

        return            

    def set_var(self , name : str , new_val : str) -> bool:

        file_data : str = ""
        found : bool = False
        with open(self.path , 'r+') as file:
            for line in file: 
                if line.find(name) != -1:
                    line = f"{name}: {new_val}\n"
                    found = True
                    # we do not exit the loop because we still add every line of the config line in the string

                file_data += line            
            #
        #
        
        if found == False:
            logging.error(f"The variable {name} does not exist")
            return False
        
        with open(self.path, 'w') as file:
            file.write(file_data)
        return True
    def set_vars(self , args):
        success_cnt = 0 
        for expression in args:
            string_data = expression.split('=',1)
            if len(string_data) != 2:
                continue

            success_cnt += self.set_var(string_data[0], string_data[1]) 
        #  
        if success_cnt == 0:
            logging.info("No changes occured to the config file")
        elif success_cnt == len(args):
            logging.info("All changes were saved succesfully")
        else:
            failed_ops = len(args) - success_cnt
            plural = str(int(failed_ops != 1) )
            if plural == "0":
                plural = ""
            else:
                plural = "s"

            logging.info(f"{failed_ops} operation{plural} failed. {success_cnt} succeeded.")
        return
    #
    def get_var(self , name : str) -> str:
        return self.file_vars[name]
    
    def print_data(self) -> None:
        for key , value in self.file_vars.items():
            logging.info(f"{key} : {value}")
        return
    #
   
#

# the arguments are interpreted as <VAR>=<VAL> expressions
def process_config_expressions(args):
    config_file = ConfigFileManager("./res/config.config")
    config_file.set_vars(args.expressions)
    return
#
