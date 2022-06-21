# Create Whl With DLL

This is a simple example to package a python whl with C++ dll. </br>

    .
    ├── test_whl test_whl              # Folder contain main python file and dll (folder name will be the name use in "import")
    │   ├── __init__.py                # python file import main python file
    │   ├── hello_world_pywrapper.py   # main python file
    │   └── test_hello_world.dll       # C++ dll
    ├── hello_world_main.py
	├── LICENSE
	├── README.md
	└── setup.py       # setup commmand for building whl
	
To create the wheel file, run the following command in a python terminal.
```
python setup.py bdist_wheel
```
Output file in dist/test_whl-1.0.0-py3-none-any.whl

Run the following command to install package.
```
pip install dist/test_whl-1.0.0-py3-none-any.whl
```
Show package info:
```
pip show test_whl
```
Test to import package:
```
python hello_world_main.py
```
Command will show:
```
Hello World
Have a nice day!
```
For more info about ```__init__.py```, please refer to https://towardsdatascience.com/whats-init-for-me-d70a312da583 
