__author__ = 'hatice'


import sys
import concatenate

def command_line_fun():



    #These lines of code allow the python script to be called directly from bash with the arguments of the main function. For this, need to define what the main function of the script is.
    if __name__ == "__main__":
        concatenate.function_concatenate(str(sys.argv[1]), str(sys.argv[2]),  str(sys.argv[3]))



    #function_concatenate('sample1', 'R1.gz', 'R2.gz')





