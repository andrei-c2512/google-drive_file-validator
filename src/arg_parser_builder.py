import argparse
from config_vars import ConfigVars
from config_file_management import ConfigFileWriter
import file_filter 

def build_validate_parser(subparser):

    validate_parser = subparser.add_parser("validate" , help="Validate the liftime of files in a specific drive folder")

    validate_parser.add_argument("-d", "--driveId", required=False, default=ConfigVars.defaults["DRIVE_ID"],
                                 help="The driveId of drive that the validator is going to access")
    validate_parser.add_argument("-f", "--folderId", required=False,default=ConfigVars.defaults["FOLDER_ID"],
                                 help="The folderId of the folder that is going to be accessed "
    "from a specifc drive")

    validate_parser.add_argument("-l" , "--lifetime" , required=False , default=ConfigVars.defaults["LIFETIME"],
                                 help ="The lifetime of the files")
    validate_parser.add_argument("-p" , "--pattern" , required=False , default=ConfigVars.defaults["DATE_PATTERN"],
                                 help="The pattern of the files that are going to be saved" " despite being expired.\n "
                                      "The pattern is the following: YYYY-MM-DD")

    validate_parser.add_argument("--force" ,
                                 help="If this flag is used,  it does not ask you to confirm the files you want to delete",
                                 action="store_true",
                                 required=False)
    validate_parser.add_argument("-g" , "--glob" , required=False, default=ConfigVars.defaults["GLOB"],
                                 help="Specifies the glob pattern that is going to be used on each file")
    validate_parser.add_argument("-r" , "--regex" , required=False , default=ConfigVars.defaults["REGEX"],
                                 help="Specifies the regex that is going to be used on each file")

    validate_parser.set_defaults(func=file_filter.validate_a)
    return
#
def build_config_parser(subparser) -> None:
    config_parser = subparser.add_parser("config" , help="Set certain variables in the config file")
    config_parser.add_argument("expressions" , nargs="*", help = "List of expressions")
    config_parser.add_argument("-l","--list",required=False, action="store_true",help="List all of the config file contents")
    config_parser.set_defaults(func=ConfigFileWriter.update_config)
    return
#

def build_arg_parser():
    parser = argparse.ArgumentParser(
        description="Delete files depending on the lifetime you configured. The program only works on *common drives*",
        epilog="Project done by Leafy Alex and Sheepherder Alex"
    )
    
    # manager = conf.ConfigFileManager("res/config.config")
     
    subparser = parser.add_subparsers(dest="command" , required=True , help="Available commands")
    build_validate_parser(subparser)
    build_config_parser(subparser)
    return parser

    
