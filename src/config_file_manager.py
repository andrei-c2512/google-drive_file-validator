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
                if line[0] == '#':
                    continue 
                parts = line.split(':', 1)
                if len(parts) != 2:
                    continue;
                # we remove the end of line character if it has one , because it is annoying
                if parts[1][len(parts[1]) -1] == '\n':
                    parts[1] = parts[1][:-1]
                self.file_vars.update( { parts[0] : parts[1]})
                
        return            

    def set_var(self , name : str , new_val : str) -> None:

        file_data : str = ""
        with open(self.path , 'r+') as file:
            for line in file: 
                if line.find(name) != -1:
                    line = f"{name}: {new_val}\n"

                file_data += line            
            #
        #

        with open(self.path, 'w') as file:
            file.write(file_data)

    def get_var(self , name : str) -> str:
        return self.file_vars[name]
    
    def print_data(self) -> None:
        for key , value in self.file_vars.items():
            logging.info(f"{key} : {value}")
        return
