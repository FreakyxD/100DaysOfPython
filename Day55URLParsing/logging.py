inputs = [1, 2, 3]


def logging_decorator(function):
    def wrapper(*args):
        a = args[0]
        b = args[1]
        c = args[2]

        print(f"You called {function.__name__}({a}, {b}, {c})")
        result = function(a, b, c)
        print(f"It returned: {result}")
        return result
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
