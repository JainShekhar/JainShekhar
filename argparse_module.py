#argparse makes the command line arguments passed to python scripts stored in sys.argv more interacctive and meaningful.
#The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
#see for details https://www.geeksforgeeks.org/command-line-option-and-argument-parsing-using-argparse-in-python/

import argparse
  
  
# Step 1: Initializing Parser: there are other parameters but here is only the parameter description or the text that is displayed
parser = argparse.ArgumentParser(description ='sort some integers.')
  
# Step 2: Adding Argument(s): there are multiple parameters

# the first argument is reading all the arguments in the command line
# the parameters for this argument are:
# first parameter is the description or the text that is displayed
# metavar is just the name of the argument in usage messages
# type is the type to which the command line arguments are converted to
# nargs is the number of arguments, here '+' just means it can take multiple numbers
# help is the brief description that is displayed 
parser.add_argument('integers',
                    metavar ='N',
                    type = float,
                    nargs = '+',
                    help ='integer(s) for the accumulator')

# the second argument is for getting the sum; action is store the value after sum while const does the sum
parser.add_argument('sum',
                    action ='store_const',
                    const = sum)

# the third argument is the getting the number of integers; action is store the result for the number of integers after const calculates len  
parser.add_argument('len',
                    action ='store_const',
                    const = len)

#Step 3: parsing Argument(s)  
args = parser.parse_args()

add = args.sum(args.integers)
length = args.len(args.integers)
average = add / length
print(average)


