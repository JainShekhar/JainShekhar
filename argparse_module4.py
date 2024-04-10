import argparse

def factorial(n):
    print(n)
    fact = 1    
    for i in range(1,n+1):
        fact *= i
    return fact

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Return the factorial of the integer")

    parser.add_argument("integer", type = int, help="Input integer", nargs=1)
    
    args = parser.parse_args()
    
    input = args.integer[0]
    result = factorial(input)
    print(f'Factorial of {input} is {result}') 

