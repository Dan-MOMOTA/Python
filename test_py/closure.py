def adder(x):
    def wrapper(y):
        return x+y
    return wrapper
adder5 = adder(5)
print(adder5(adder5(6))) #16