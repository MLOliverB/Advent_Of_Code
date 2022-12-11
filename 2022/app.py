import sys
from importlib import import_module

def get_solve_function(day_number):
    name = f"day_{day_number}"
    module = None
    try:
        module = import_module(f".{name}", package="src")
    except ImportError as e:
        print ("module not found: " + name + ' - ' + str(e))
    if module != None:
        solve_func = getattr(module, "solve")
        return solve_func
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) == 3:
        day = int(sys.argv[1])
        text_input_file = sys.argv[2]
        solve_func = get_solve_function(day)
        if solve_func == None:
            print(f"Could not retrieve the solve function for day {day}")
        else:
            solve_func(day, text_input_file)
    else:
        raise ValueError("Program needs two arguments: [day number] [input file name]")