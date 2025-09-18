# crs2ini converter
crs2ini is a tool that converts CRS files made by the editor [Realworld Cursor Editor] [rwce] into INF files that can install the cursor pack.
## Usage
```batch
python main.py file.crs [flags]
```
## Flags
- If you input a file without any args, the tool will ask for a custom name for the cursor set. This can be bypassed with the `-n` or `--name` flag with the custom name of the cursor set. Example:
    ```sh
    python main.py file.crs -n Custom Scheme
    ```
- If you want to have the .inf file in another directory or as another file, you can use the flag `-o` or `--output` followed by the path of the output path. Example:
    ```sh
    python main.py file.crs -o "C:\path\to\cursor\installer.inf"
    ```
    The default path will be the original directory of the .crs file, followed by the name of the file, which by default will be `install.inf`
    
- [EXPERIMENTAL] Using the `-i` or `--install` flag will install the cursors file given by the converter. 
    _IMPORTANT!_ The path of the install file has to be the same path of the cursors, and the script must be executed with administrative permissions.

## License
Licensed under the CC0 v1.0 license.

[rwce]: <https://www.rw-designer.com/cursor-maker>
