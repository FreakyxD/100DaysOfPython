import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # do something before
        function()
        # function() - can also run it multiple times
        # do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


say_hello()

# how this can also be done
# decorated_function = delay_decorator(say_hello)
# decorated_function()

# say_greeting() - no delay
# say_bye() - delay
