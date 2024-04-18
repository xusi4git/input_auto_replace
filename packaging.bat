@REM pyinstaller -F -n input_auto_replace.exe --add-data=./config.toml:./config.toml main.py 
@REM 使用upx --upx-dir="e:/workzone/software/upx-4.2.2-win64/upx"
pyinstaller -F -n input_auto_replace.exe   --add-data=./config.toml:./config.toml main.py 