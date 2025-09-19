# Pass all arguments from PowerShell to main.py in the 'app' folder

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$pythonScript = Join-Path $scriptDir 'app\main.py'

python $pythonScript @args