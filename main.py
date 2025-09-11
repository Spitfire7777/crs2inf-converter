import sys, configparser

def create_inf_file(name, file, verbose=False, only_convert=False, output_path=""):
            
    # Read the cursor scheme configuration file
    file = sys.argv[1]
    with open(file, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    cur_file = configparser.ConfigParser()
    cur_file.read_string(content)

    cur_dir = {}
    for cursor in cur_file.sections():
        for _, value in cur_file.items(cursor):
            cur_dir[cursor] = value

    # Prepare INF installer configuration
    inf_installer = configparser.ConfigParser(allow_no_value=True)
    inf_installer['Version'] = {
        'Signature': '$CHICAGO$',}
    inf_installer['DefaultInstall'] = {
        'CopyFiles': 'Scheme.Cur,',
        'AddReg': 'Scheme.Reg'}
    inf_installer['DestinationDirs'] = {
        'Scheme.Cur': '10,"%%CUR_DIR%%"',
        'Scheme.Txt': '10,"%%CUR_DIR%%"'}
    

    # Checking and adding cursor directories, files and associations if they exist for the Registry
    main_header = 'HKCU,"Control Panel\\Cursors\\Schemes","%SCHEME_NAME%",'
    dirs, files = [], []
    cursors = {}        

    for key in cur_dir:
        files.append(cur_dir[key]['Path'])
        match key:
            case 'Arrow':
                dirs.append(r'%10%\%CUR_DIR%\%pointer%')
                cursors['pointer'] = cur_dir[key]['Path']
            case 'Help':
                dirs.append(r'%10%\%CUR_DIR%\%help%')
                cursors['help'] = cur_dir[key]['Path']
            case 'AppStarting':
                dirs.append(r'%10%\%CUR_DIR%\%work%')
                cursors['work'] = cur_dir[key]['Path']
            case 'Wait':
                dirs.append(r'%10%\%CUR_DIR%\%busy%')
                cursors['busy'] = cur_dir[key]['Path']
            case 'Crosshair':
                dirs.append(r'%10%\%CUR_DIR%\%cross%')
                cursors['cross'] = cur_dir[key]['Path']
            case 'IBeam':
                dirs.append(r'%10%\%CUR_DIR%\%text%')
                cursors['text'] = cur_dir[key]['Path']
            case 'NWPen':
                dirs.append(r'%10%\%CUR_DIR%\%hand%')
                cursors['hand'] = cur_dir[key]['Path']
            case 'No':
                dirs.append(r'%10%\%CUR_DIR%\%unavailiable%')
                cursors['unavailiable'] = cur_dir[key]['Path']
            case 'SizeNS':
                dirs.append(r'%10%\%CUR_DIR%\%vert%')
                cursors['vert'] = cur_dir[key]['Path']
            case 'SizeWE':
                dirs.append(r'%10%\%CUR_DIR%\%horz%')
                cursors['horz'] = cur_dir[key]['Path']
            case 'SizeNWSE':
                dirs.append(r'%10%\%CUR_DIR%\%dgn1%')
                cursors['dgn1'] = cur_dir[key]['Path']
            case 'SizeNESW':
                dirs.append(r'%10%\%CUR_DIR%\%dgn2%')
                cursors['dgn2'] = cur_dir[key]['Path']
            case 'SizeAll':
                dirs.append(r'%10%\%CUR_DIR%\%move%')
                cursors['move'] = cur_dir[key]['Path']
            case 'UpArrow':
                dirs.append(r'%10%\%CUR_DIR%\%alternate%')
                cursors['alternate'] = cur_dir[key]['Path']
            case 'Hand':
                dirs.append(r'%10%\%CUR_DIR%\%link%')
                cursors['link'] = cur_dir[key]['Path']
            case _:
                print(f"Warning: Unknown cursor type '{key}' found in configuration.")

    scheme_value = main_header + '"' + ",".join(d for d in dirs) + '"'
    print(scheme_value)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename> [options]")
        sys.exit(1)
    
    verbose, only_convert = False, False
    c_scheme_name, output_path = "" , ""
    args = sys.argv[2:]
    
    for arg in args:
        if add_name:
            c_scheme_name = arg
            add_name = False
            continue    
        match arg:
            case '-h' | '--help':
                print("Usage: python main.py <filename>")
                sys.exit(0)
            case "-v" | "--version":
                print("Cursor Scheme Converter Version 1.0")
                sys.exit(0)
            case "-n" | "--name":
                if len(args) > args.index(arg) + 1:
                    c_scheme_name = args[args.index(arg) + 1]
            case "-V" | "--verbose":
                verbose = True
            case "-c" | "--convert":
                only_convert = True
            case "-o" | "--output":
                if len(args) > args.index(arg) + 1:
                    output_path = args[args.index(arg) + 1]
            case _:
                if arg.startswith('-'):
                    print(f"Unknown option: {arg}")
                    sys.exit(1)

    name = input("Enter cursor scheme name: ") if not c_scheme_name else c_scheme_name

    create_inf_file(name, sys.argv(1), )
        

if __name__ == "__main__":
    main()