def safe_divide(numerator, denominator):

    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return numerator/denominator
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."