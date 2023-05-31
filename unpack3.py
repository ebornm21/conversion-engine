#A program that uses the capabilities of args and kwargs to define the different variables and return them.

def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)


f(100, 50, 25, galleons=100, sickles=50, knuts=25)