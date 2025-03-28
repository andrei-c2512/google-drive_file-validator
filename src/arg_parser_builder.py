import argparse
from config_file_manager import ConfigFileManager
from config_file_manager import process_config_expressions
from file_filter import *


def build_validate_parser(subparser):
    manager = ConfigFileManager("res/config.config")

    validate_parser = subparser.add_parser("validate" ,
                                           help="Validate the liftime of files in a specific drive folder")
    validate_parser.add_argument("-d", "--driveId", required=False, default=manager.get_var("DRIVE_ID"),
                                 help="The driveId of drive that the validator is going to access")
    validate_parser.add_argument("-f", "--folderId", required=False,default=manager.get_var("FOLDER_ID"),
                                 help="The folderId of the folder that is going to be accessed "
    "from a specifc drive")

    validate_parser.add_argument("-l" , "--lifetime" , required=False , default=manager.get_var("LIFETIME"),
                                 help ="The lifetime of the files")
    validate_parser.add_argument("-p" , "--pattern" , required=False , default=manager.get_var("PATTERN"), 
                                 help="The pattern of the files that are going to be saved" " despite being expired.\n "
                                      "The pattern is the following: YYYY-MM-DD")

    validate_parser.add_argument("--force" ,
                                 help="If this flag is used,  it does not ask you to confirm the files you want to delete",
                                 action="store_true",
                                 required=False)

    validate_parser.set_defaults(func=validate_a)
    return
#
def build_config_parser(subparser) -> None:
    config_parser = subparser.add_parser("config" , help="Set certain variables in the config file")
    config_parser.add_argument("expressions" , nargs="*", help = "List of expressions")
    config_parser.set_defaults(func=process_config_expressions)
    return
#

def build_arg_parser():
    parser = argparse.ArgumentParser(
        description="Delete files depending on the lifetime you configured. The program only works on *common drives*",
        epilog="Project done by Leafy Alex and Sheepherder Alex"
    )
    
    manager = ConfigFileManager("res/config.config")
     
    subparser = parser.add_subparsers(dest="command" , required=True , help="Available commands")
    build_validate_parser(subparser)
    build_config_parser(subparser)
    return parser

    
