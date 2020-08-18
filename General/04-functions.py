# Functions

# Basic function
def func1():
    print("I am a function")


# Functions that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)


def cube(x):
    return x*x*x


# function with default value for an argument

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


# function with variable number of arguments

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


# derftgytrefwdszDSF(*&^TY!)
# hamivem836@mado34.com


# Output
print("func1 results:")
func1()
print(func1())
print(func1)


# Fun2 Output
print("func2 results:")
func2(10, 20)
print(func2(10, 20))
print(cube(3))


# func power output
print("Power func results:")
print(power(2))
print(power(2, 3))
print(power(x=3, num=2))


print(multi_add(4, 5, 10, 4))
