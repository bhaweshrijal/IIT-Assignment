def main():
    try:
        n = int(input("Enter a non-zero integer: "))
        if n != 0:
            r = 1 / n
            print("The reciprocal of {0} is {1:,.3f}".format(n, r))
    except ValueError as value:
        print(f"{value}, please enter a valid number.")
        return
    except ZeroDivisionError as zero:
        print(f"{zero}. You entered zero. Please try again.")
        return
    finally:
        print("Thank you for using our program.")
main()                      