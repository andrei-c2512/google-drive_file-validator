import logging
from .config_sanity_checker import ConfigSanityChecker
from .config_vars import ConfigVars

# checks if a config.sh exists
ConfigSanityChecker.run()
# updates the variables in this order: enviroment -> config file -> hard coded values
ConfigVars.run()
# logging set up
logging.basicConfig(level=logging.INFO)
logging.getLogger("googleapiclient").setLevel(level=logging.ERROR)
logging.getLogger("oauth2client").setLevel(level=logging.ERROR)

