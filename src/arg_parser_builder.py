import argparse



def build_arg_parser():
    parser = argparse.ArgumentParser(
        description="Delete files depending on the lifetime you configured. The program only works on *common drives*",
        epilog="Project done by Leafy Alex and Sheepherder Alex"
    )
    subparser = parser.add_subparsers(dest="command" , required=True , help="Available commands")

    validate_parser = subparser.add_parser("validate" , help="Validate the liftime of files in a specific drive folder")
    validate_parser.add_argument("-l" , "--lifetime" , required=False , help ="The lifetime of the files")
    validate_parser.add_argument("-p" , "--pattern" , required=False , help="The pattern of the files that are going to be saved"
    " despite being expired.\n "
    "The pattern is the following: YYYY-MM-DD")
    validate_parser.add_argument("-d", "--driveId", required=False, help="The driveId of drive that the validator is going to access")
    validate_parser.add_argument("-f", "--folderId", required=False, help="The folderId of the folder that is going to be accessed "
    "from a specifc drive")

    config_parser = subparser.add_parser("config" , help="Set certain variables in the config file")
    
