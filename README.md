*CLI app made to manage files stored in Google Drive.*

# Table of contents

1. [Set-up](#set-up)
2. [Usage](#usage)
3. [For developers](#fordevelopers)
 

## Set-up:

### Google API shenanigans

For this program to work you need to create a [Google Service Account](https://cloud.google.com/iam/docs/service-accounts-create)  
Then go to a `Common Drive` and give it , depending on your usage , the following perms:  
- Content Manager -> to only manage files created by the same service account
- Manager         -> to manage all files 

### Giving access 

To let the program access your account , please create a valid JWT for it. To do so:  

1. Go to Google Console 
2. APIs (to do left)
3. Credentials 
4. Go to Service Accounts on the lower half
5. Create a service account 
6. Click on it 
7. Go to keys tab
8. Create a key and download it
9. Rename it to `credentials.json` and move it to `./res/` to be accessed by the program

### Downloading the libraries: 

```shell
    # if you are on anything that uses pip
    make set-up-pip
    # if you are on debian(the system that I developed on)
    make set-up-debian
```

## Usage

### The `validate` command
It is made to process files with the following format:  

`<DATE>_<TIME>_<FILE_NAME>.<EXTENSION>`  

To be more precise:  

`YYYY-MM-DD_HH-MM-SS_FILE.<something>`

### How to use:
```shell
   python3 src/main.py -d <drive_id> -f <folder_id> -l <lifetime> -p <date_pattern>
```
Flags explained:
- `-d/--driveId`  -> specify the target drive that you want the process to run on
- `-f/--folderId` -> specify the target folder from within a drive
- `-l/--lifetime` -> set the max lifetime of the files that are not going to be deleted
- `-p/--pattern`  -> provide a pattern that is going to save files from being delete  
For example:
    `YYYY-MM-15` is going to except files that were created on the 15th day of any month and year
- `--force` -> by default , the CLI asks you to confirm the files that are going to be deleted. By adding this flag ,
you can now peacefully run this command in your script

### The `config` command

Every flag specified above is *optional*. If a flag is not present , the it will get it's default value from:  
`./res/config.config`

To see all the variables in the config file , please use the following:  
`python3 src/main.py config --list`

To set a variable from within the terminal, use:  
`python3 src/main.py <VAR_1>=<VALUE_1>  <VAR_2>=<VALUE_2> ... (you can list as much as you like)`

### The `delreg` command
The regular expression delete command  
`python3 src/main.py delreg -d <DRIVE_ID> -f <FOLDER_ID> -r <REGEX>`  
This command is reserved for certified cracked devs who know regular expressions ( I am not one )   

> Note: Not specifying the driveId or folderId will result in using the `config.config` variables  


### The `delg` command
The `glob` expression delete command.  
A glob expression is similar to the ones you use in a .gitignore/makefile/any file filtering terminal command  
Example of glob expressions:  

```shell
# get any file that ends in FII_CODE.zip
*FII_CODE.zip
# gets any file that contains 03-
*03-*
# get any file that starts with 2025
2025*
```
## For developers:

### General:
- if you are in ASII and need some features , ask me or request to make you a collaborator
- contact me or Frunza Alexandru if you have a problem with setting up a Service Account
Code:
- if you develop on a different system , please add the set-up as a rule in the `makefile`  

### Coding practices:
- use `logging` for printing - [Tutorial](https://www.youtube.com/watch?v=urrfJgHwIJA)
- use `unittest` module for testing - [Tutorial](https://www.youtube.com/watch?v=6tNS--WetLI)
- any new external files should be put in the `./res/` directory