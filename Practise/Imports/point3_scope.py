# the local scope of one function can't use variables
# from another function's local scope

def first():
    loc = 2
    return loc

def sec():
    return loc


first()
sec()