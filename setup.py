# Importing and installing (if do not exist) all necessary libraries

import os

required = ["opencv-python","tkinter"]

def setup(package):
    try:
        __import__(package)
        print("imported ", package)
    except ImportError:
        os.system("pip install "+ package)
        print("installing ",package) 

for x in required:
    setup(x)


  
 


