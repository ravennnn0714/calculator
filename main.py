import time

print("Calculator")

def line():
  print("----------")

time.sleep(.25)
line()

num1 = float(input("ENTER THE FIRST NUMBER: "))
num2 = float(input("ENTER THE SECOND NUMBER: "))

operatorCheck = True
while operatorCheck == True:
  operator = input("ENTER THE OPERATOR (+, -, x, /): ")
  if(operator == "+") or (operator == "-") or (operator == "x") or (operator == "/"):
    operatorCheck = False
    break
  line()
  print("Invalid answer.")


def calculate(num1, num2, operator):
  if operator == "+":
    result = num1 + num2
  if operator == "-":
    result = num1 - num2
  if operator == "x":
    result = num1 * num2
  if operator == "/":
    result = num1 / num2

  return result


print("The result is:")
print(calculate(num1, num2, operator))