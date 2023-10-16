@echo off
echo Installing requirements...
pip install -r requirements.txt
echo Requirements installed successfully!

echo Creating start.bat...
echo @echo off > start.bat
echo python main.py >> start.bat
echo start.bat created!

echo Deleting setup.bat...
del setup.bat
echo setup.bat deleted!

echo Installation completed. Enjoy!