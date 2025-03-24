

class ConfigFileManager:
    def __init__(self , path):
        self.path = path
        self.file_vars : dict[str, str] = {}
        with open(path , 'r') as file:
            line : str = file.readline()
        
            while line:
                if line[0] == '#':
                    continue
                
                parts = line.split(':', 1)
                line : str = file.readline()
                self.file_vars.update( { parts[0] : parts[1]})
            

    def set_var(self , name : str , newVal : str) -> None:
        self.file_vars[name] = newVal
        with open(self.path , 'w') as file:
            file_content = file.read(-1)
            
            #files in config files are like this : variableName: <value>
            str_to_find = name + ":"

            variable_value_start = file_content.find() + len(str_to_find)

            print(file_content)

        return
    
    def get_var(self , name : str) -> str:
        return self.file_vars[name]
    
    def print_data(self) -> None:
        for key , value in self.file_vars.items():
            print(f"{key} : {value}")
        return
