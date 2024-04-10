#sys.argv stores the command line arguments when calling the python script
#sys.argv[0] is the name of the python script
# see for more details: https://www.geeksforgeeks.org/python-sys-module/
import sys

n = len(sys.argv)
print("Total arguments passed:", n)
  
# Arguments passed
print("\nName of Python script:", sys.argv[0])
  
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
      
# Addition of numbers
Sum = 0
  
for i in range(1, n):
    Sum += int(sys.argv[i])
      
print("\n\nResult (sum of numbers):", Sum)
