# local variables can't be used by code  in the global scope
def local_exe():
    breakfast = "waffles"
    return breakfast
local_exe()
print(breakfast)