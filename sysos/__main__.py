import os
import sys
import os.path

def main():
    arg = sys.argv
    print(arg[0], arg[1])
    path = './' + arg[1]
    print(os.path.isfile(path))

if __name__ == "__main__": 
	main()
