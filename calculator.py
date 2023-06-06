# calculator.py
# calculator function

# add function
def add(x,y):
  return x + y

# Substract function
def substract(x,y):
  return x - y

# multiply function
def multiply(x,y):
  return x * y

# divide function
def divide(x,y):
  if y == 0:
    raise ValueError("divisor cannot be 0")
  return x / y