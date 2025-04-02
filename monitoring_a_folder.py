import os
import sys
import sched
from difflib import Differ  # Import Differ from difflib

def monitor():

    path = "C:\\Users\\saradha.b\\downloads"
    dir_list = os.listdir(path)
    print (f"the list of files in downloads:\n")
    # Redirect stdout to a file
    with open('new_output.txt', 'w') as f:
        sys.stdout = f
        for file in dir_list:
            print(file)

    with open('file1.txt') as file_1, open('file2.txt') as file_2: 
        differ = Differ() 
  
    for line in differ.compare(file_1.readlines(), file_2.readlines()): 
        print(line) 
               

    sched.scheduler.every(5).seconds.do(monitor)             