# Challenge 2: Implement a Calculator Class

class Calculator:
    def __init__(self):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        print(self.num1 + self.num2)

    def subtraction(self):
        print(self.num2 - self.num1)

    def multiplication(self):
        print(self.num1 * self.num2)

    def division(self):
        print(self.num2 / self.num1)

num1 = float(input("Enter the number :"))
num2 = int(input("Enter the number :"))
    
cal_obj = Calculator()
cal_obj.addition()
cal_obj.subtraction()
cal_obj.multiplication()
cal_obj.division()
print(cal_obj)