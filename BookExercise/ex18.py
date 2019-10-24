# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# *arg is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("I got nothing.")


print_two("zed", "Shaw")
print_two_again("zed", "Shaw")
print_one("First!")
print_none()


# try by meysef
def print_two_try(*ar):
    arg1, arg2 = ar
    print(f"arg1: {arg1}, arg2: {arg2}")


print_two_try("valerie", "lai")
