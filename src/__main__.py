from . import arg_parser_builder as cli


def main():
   parser = cli.build_arg_parser() 
   args = parser.parse_args()

   args.func(args)

if __name__ == "__main__":
    main()
