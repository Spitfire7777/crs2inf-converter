import configparser, os, ctypes

def create_inf_file(name, file, output_path: str):
    
    o_file = output_path if output_path.endswith('.inf') else os.path.join(output_path, 'install.inf')

    # Ensure output path is a directory if it doesn't end with .inf
    if not os.path.exists(o_file) and not o_file.endswith('.inf'):
        os.makedirs(o_file)
    
    print(f"Output directory set to: {o_file}")

    # Read the cursor scheme configuration file
    with open(file, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    cur_file = configparser.ConfigParser()
    cur_file.read_string(content)

    cur_dir = {}
    for cursor in cur_file.sections():
        for _, value in cur_file.items(cursor):
            cur_dir[cursor] = value

    # Checking and adding cursor directories, files and associations if they exist for the Registry
    
    dirs, cursors, files = {}, [], []
    for _ in range(17): cursors.append(None)
    order = ['pointer', 'help', 'work', 'busy', 'cross', 'text', 'hand', 'unavailiable',
             'vert', 'horz', 'dgn1', 'dgn2', 'move', 'alternate', 'link', 'pin', 'person']

    for key in cur_dir:
        files.append(cur_dir[key])
        type = ""
        match key:
            case 'Arrow':       type = 'pointer'
            case 'Help':        type = 'help'
            case 'AppStarting': type = 'work'
            case 'Wait':        type = 'busy'
            case 'Crosshair':   type = 'cross'
            case 'IBeam':       type = 'text'
            case 'NWPen':       type = 'hand'
            case 'No':          type = 'unavailiable'
            case 'SizeNS':      type = 'vert'
            case 'SizeWE':      type = 'horz'
            case 'SizeNWSE':    type = 'dgn1'
            case 'SizeNESW':    type = 'dgn2'
            case 'SizeAll':     type = 'move'
            case 'UpArrow':     type = 'alternate'
            case 'Hand':        type = 'link'
            case 'Pin':         type = 'pin'
            case 'Person':      type = 'person'
            case _: print(f"Warning: Unknown cursor type '{key}' found in configuration.")
        
        print(f"Mapping cursor '{key}' to file '{cur_dir[key]}' as type '{type}'")
        if type in order:
            print(f"Found cursor type '{type}' at index {order.index(type)}")
            dirs[type] = r'%10%\%CUR_DIR%\%'+type+'%'
            cursors[order.index(type)] = cur_dir[key]
        else:
            print(f"Cursor type '{type}' not in predefined order list.")
        type = ""

    main_header = 'HKCU,"Control Panel\\Cursors\\Schemes","%SCHEME_NAME%",,"'
    key_list = ""
    for ord in order:
        if ord in dirs.keys():
            key_list += dirs[ord] + ','
    scheme_value = main_header + key_list.rstrip(",") + '"'
    cur_txt = r'10,"%CUR_DIR%"'

    # Prepare INF installer configuration
    inf_installer = configparser.ConfigParser(allow_no_value=True, interpolation=None)
    inf_installer.optionxform = str # type: ignore # Preserve case sensitivity
    inf_installer['Version'] = {
        'Signature': '$CHICAGO$',}
    inf_installer['DefaultInstall'] = {
        'CopyFiles': 'Scheme.Cur,',
        'AddReg': 'Scheme.Reg'}
    inf_installer['DestinationDirs'] = {
        'Scheme.Cur': cur_txt,
        'Scheme.Txt': cur_txt}
    inf_installer['Scheme.Reg'] = { # type: ignore
        scheme_value: None}
    inf_installer['Scheme.Cur'] = { # type: ignore
        f'"{f}"': None for f in files}
    inf_installer['Strings'] = { 
        'CUR_DIR': name,
        'SCHEME_NAME': name,
        **{k : v for k, v in zip(order, cursors) if v is not None}
    }

    # Write the INF file
    with open(o_file, 'w', encoding='utf-8') as inf_file:
        inf_installer.write(inf_file)
    
    return o_file

def install_inf_file(inf_path):
    """
    Installs a .inf file on Windows using rundll32.
    Requires administrative privileges, so the user will be prompted for elevation.
    """
    if not os.path.isfile(inf_path):
        raise FileNotFoundError(f"{inf_path} does not exist.")
    cmd = f"rundll32.exe setupapi,InstallHinfSection DefaultInstall 132 {inf_path}"
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/c {cmd}", None, 1)
        print(f"Successfully installed {inf_path}")
    except Exception as e:
        print(f"Failed to install {inf_path}: {e}")
