x=3

def hello():
    x=5
    print(f"the local variable is {x}")

print(f"the global variable is {x}")
hello()
print(f"the global variable is {x}")


# How to convert global variable into local variable
x = 10  # global variable


def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable
  print(y)


my_function()
print(x)

# But its still better not to change global variable within the scope of a function