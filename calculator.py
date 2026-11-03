class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b==0:
            return "undefind"
        negative = (a<0)!=(b<0)
        a=abs(a)
        b=abs(b)
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if negative:
            result = -result
        return result
    
    def modulo(self, a, b):
        if b==0:
            return "undefind"
        abs_b=abs(b)
        abs_a=abs(a)
        while abs_a >= abs_b:
            abs_a = self.subtract(abs_a,abs_b)
        return abs_a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: addition: ", calc.add(-1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
