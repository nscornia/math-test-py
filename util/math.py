
def addition(num1, num2):
  return num1 + num2


def subtraction(num1, num2):
  return num1 - num2


def multiplication(num1, num2):
  return num1 * num2


def division(num1, num2):
  return num1 / num2


def toMathFn(operator):
  if operator == "+":
    return addition
  elif operator == "-":
    return subtraction
  elif operator == "*":
    return multiplication
  elif operator == "/":
    return division
  else:
    return None
