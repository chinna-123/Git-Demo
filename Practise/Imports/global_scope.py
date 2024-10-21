# global variables can be accessed by code in a local scope
def print_glob():
    print(glob_var)


glob_var = "This is a String"
print_glob()