class MyMath:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        return base ** exponent
    
    def square_root(self, number):
        if number < 0:
            raise ValueError("Cannot compute square root of negative number")
        return number ** 0.5