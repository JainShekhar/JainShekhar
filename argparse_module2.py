#this is another example of argparse
#it returns the sum of the integers if asked for sum 
#otherwise the default return is max of the integers
import argparse

#step 1
parser = argparse.ArgumentParser(description='Process some integers.')

#step 2
#this is for reading the integers; nargs is number of command line arguments that need to be consumed
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

#this is the result: sum if --sum is the command line argument and max by default
#const is for sum and default is the max
parser.add_argument('--sum', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

#step 3
args = parser.parse_args()

print(args.sum(args.integers))
