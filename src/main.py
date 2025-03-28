
from google_api import *
from arg_parser_builder import build_arg_parser
import os

logging.basicConfig(level=logging.INFO)
logging.getLogger("googleapiclient").setLevel(level=logging.ERROR)
logging.getLogger("oauth2client").setLevel(level=logging.ERROR)



# DRIVE_ID = '1Rq8uetK6bnE6RrzMzf1QRBLUfRVSov8A'

# 
# Sa dau print la fisierele care vor fi sterse
# sa fac sa accepte argumente la linia de comanda
# optional , sa folosesc libraria de logging

def main():
   parser = build_arg_parser() 
   args = parser.parse_args()

   args.func(args)

if __name__ == "__main__":
    main()
