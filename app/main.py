import sys, convert
from os import path

def _help():
    print("Usage: crs2inf <filename> [options]\n"
          "\n"
          "Options:\n"
          "  -h, --help                 Show this help message and exit\n"
          "  -i, --install              Install the generated INF file after creation\n"
          "  -n, --name <name>          Specify the cursor scheme name\n"
          "  -o, --output <dir|file>    Specify the output directory/file for the INF file\n"
          "  -s, --silent               Run in silent mode (no prompts)\n"
          "  -v, --version              Show program version and exit\n"
          "\n")

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        _help()
        sys.exit(1)
    
    silent, install = False, False
    c_scheme_name = "Custom Scheme"  # Default name if not provided
    file, args = sys.argv[1], sys.argv[2:]
    if not path.isfile(file):
        print(f"Error: File '{file}' does not exist.")
        sys.exit(1)
    o_dir = path.dirname(file)
    
    for arg in args:   
        match arg:
            case '-h' | '--help':
                _help()
                sys.exit(0)
                break
            case "-v" | "--version":
                print("CRS to INF Converter Version 1.0")
                sys.exit(0)
                break
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
            case "-i" | "--install":    install = True
            case "-s" | "--silent":     silent = True
            case _:
                if arg.startswith('-'):
                    print(f"Unknown option: {arg}")
                    sys.exit(1)

    name = input("Enter cursor scheme name: ") if not c_scheme_name else c_scheme_name
    
    if not silent: print(f"File to convert: {file}"
          f"\nOutput directory: {o_dir}"
          f"\nConverting '{file}' with scheme name '{name}'")
    output_path = convert.create_inf_file(name, file, o_dir, silent)
    if install:
        if not silent: print(f"Installing INF file: {output_path}")
        try:
            convert.install_inf_file(output_path)
            if not silent: print(f"Successfully installed {output_path}")
        except Exception as e:
            if not silent: print(f"Failed to install {output_path}: {e}")
    else:
        if not silent: print(f"INF file '{output_path}' created successfully.\nTo install the cursor scheme, right-click the INF file and select 'Install'.")

    

if __name__ == "__main__":
    main()