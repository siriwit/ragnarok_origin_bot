del "bot\jj\roobot.exe"
del "bot\pp\roobot.exe"
del "dist\roobot.exe"
pyinstaller --name roobot entry_bot.py --onefile
xcopy "dist\roobot.exe" "bot\jj" /Y
xcopy "dist\roobot.exe" "bot\pp" /Y
