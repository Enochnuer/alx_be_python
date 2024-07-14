class ZeroDivisionError(Exception):
    def __str__(self):
        print("Error: Cannot divide by zero.")

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator/denominator
        return f"result is {result}"
    except ValueError:
        print("enter numeric value")
    except ZeroDivisionError:
        print("cannot divide by zero")


    
