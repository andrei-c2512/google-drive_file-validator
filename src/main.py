import logging
from config_sanity_checker import ConfigSanityChecker
from config_vars import ConfigVars
import arg_parser_builder as cli


# checks if a config.sh exists
ConfigSanityChecker.run()
# updates the variables in this order: enviroment -> config file -> hard coded values
ConfigVars.update_defaults()
# logging set up
logging.basicConfig(level=logging.INFO)
logging.getLogger("googleapiclient").setLevel(level=logging.ERROR)
logging.getLogger("oauth2client").setLevel(level=logging.ERROR)





def main():
   parser = cli.build_arg_parser() 
   args = parser.parse_args()

   args.func(args)

if __name__ == "__main__":
    main()
