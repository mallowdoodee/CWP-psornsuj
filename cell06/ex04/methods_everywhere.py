import sys
def shrink(arg=""):
    print(arg[:8])
    
def enlarge(arg=""):
    print(arg.ljust(8, "Z"))

if len(sys.argv) == 1:
    print("NONE")
else:
    for each in sys.argv[1:]:
        if len(each) < 8:
            enlarge(each)
        else:
            shrink(each)

    # ./methods_everywhere.py 'lol' 'physically' 'backpack'