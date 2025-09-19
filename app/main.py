import sys, convert, os

def _help():
    print("Usage: crs2inf <filename> [options]\n"
          "\n"
          "Options:\n"
          "  -h, --help                 Show this help message and exit\n"
          "  -i, --install              Install the generated INF file after creation\n"
          "  -v, --version              Show program version and exit\n"
          "  -n, --name <name>          Specify the cursor scheme name\n"
          "  -o, --output <dir|file>    Specify the output directory/file for the INF file\n"
          )

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        _help()
        sys.exit(1)
    
    verbose, install = False, False
    c_scheme_name = "Custom Scheme"
    file = sys.argv[1]
    o_dir = os.path.dirname(file)
    args = sys.argv[2:]
    
    for arg in args:   
        match arg:
            case '-h' | '--help':
                _help()
                sys.exit(0)
            case "-v" | "--version":
                print("CRS to INF Converter Version 1.0")
                sys.exit(0)
            case "-n" | "--name":
                if len(args) > args.index(arg) + 1:
                    arg_index = args.index(arg)
                    j = 1
                    for i in args[args.index(arg) + 1:]:
                        if i.startswith('-'):
                            break
                        j += 1
                    c_scheme_name = " ".join(args[arg_index + 1: arg_index + j])
            case "-o" | "--output":
                if len(args) > args.index(arg) + 1:
                    o_dir = args[args.index(arg) + 1]
            case "-i" | "--install":
                install = True
            case _:
                if arg.startswith('-'):
                    print(f"Unknown option: {arg}")
                    sys.exit(1)

    name = input("Enter cursor scheme name: ") if not c_scheme_name else c_scheme_name
    
    print(f"File to convert: {file}"
          f"\nOutput directory: {o_dir}"
          f"\nConverting '{file}' with scheme name '{name}'")
    output_path = convert.create_inf_file(name, file, o_dir)
    if install:
        print(f"Installing INF file: {output_path}")
        convert.install_inf_file(output_path)
    else:
        print(f"INF file '{output_path}' created successfully.")
        print("To install the cursor scheme, right-click the INF file and select 'Install'.")

    

if __name__ == "__main__":
    main()