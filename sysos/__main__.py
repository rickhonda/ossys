import os
import sys
import os.path
from zxcv import * 

def main():
    arg = sys.argv
    path = './' + arg[1]
    result = os.path.isfile(path)
    if result == True:
        sys.stderr.write("The file \"" + arg[1] + "\" already exists!\n")


        
if __name__ == "__main__": 
	main()
