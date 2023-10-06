def factorial(n):
    """
    Calculates the factorial of a positive
    integer number
    """
    if n == 0:
        return 1
    elif n < 0:
        return n
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def main():
    number = int(input("Enter the number to calculate factorial:\n"))
    result = factorial(number)
    print("The factorial of {0} is {1}\n".format(number, result))

if __name__ == "__main__":
    main()
