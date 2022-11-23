class Calculator:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def addition(self):
        result_val = self.value1 + self.value2
        return result_val

    def subtraction(self):
        result_val = self.value1 - self.value2
        return result_val

    def multiplication(self):
        result_val = self.value1 * self.value2
        return result_val

    def division(self):
        result_val = self.value1 / self.value2
        return result_val

    def exponent(self):
        result_val = self.value1 ** self.value2
        return result_val

    def modulus(self):
        result_val = self.value1 % self.value2
        return result_val


try:
    input_val1 = int(input('> '))
    input_operation = input('> ')
    input_val2 = int(input('> '))
except ValueError or NameError:
    print('invalid')
    input_val1 = None
    input_operation = None
    input_val2 = None

error = True

if input_val1 and input_val2 and input_operation is not None:
    if '+' in input_operation and len(input_operation) == 1:
        error = False
        calc = Calculator(input_val1, input_val2)
        print(calc.addition())

    if '-' in input_operation and len(input_operation) == 1:
        error = False
        calc = Calculator(input_val1, input_val2)
        print(calc.subtraction())

    if '*' in input_operation and len(input_operation) == 1:
        error = False
        calc = Calculator(input_val1, input_val2)
        print(calc.multiplication())

    if '/' in input_operation and len(input_operation) == 1:
        error = False
        calc = Calculator(input_val1, input_val2)
        print(calc.division())

    if '**' in input_operation and len(input_operation) == 2:
        error = False
        calc = Calculator(input_val1, input_val2)
        print(calc.exponent())

    if '%' in input_operation and len(input_operation) == 1:
        error = False
        calc = Calculator(input_val1, input_val2)
        print(calc.modulus())

    if len(input_operation) > 2:
        error = True

    try:
        if error is True:
            print('invalid')
    except NameError:
        pass
