#sys module provides various functions and variables that are used to manipulate different parts of the Python runtime environment
#for more details see https://www.geeksforgeeks.org/python-sys-module/
import sys

#print current version of python
print(f'Current version of Python: {sys.version}')

#stdin takes input from command line
print(f'Enter your input or type q to exit')
for line in sys.stdin:
    if 'q' == line.rstrip():
       break
    print(f'Your Input is: {line}')
    print(f'type q to exit')

#stdout just displays output on the command line/screen
#all standard print outputs are first written to stdout
sys.stdout.write("Exit")
print('')

#stderr whenever an exception occurs it is written to stderr
def print_to_stderr(*a): 
  
    # Here a is the array holding the objects 
    # passed as the argument of the function 
    print(*a, file = sys.stderr) 
  
print_to_stderr("Hello World")

print('sys.path module returns the list of directories that interpreter will search for required module such as pandas or numpy')
print(sys.path)
print('')

print('sys.modules return the name of the Python modules that the current shell has imported')
print (sys.modules)
