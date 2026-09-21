import sys
if len(sys.argv) >= 2:
    if sys.argv[1].count("z") > 0:
        for i in range(sys.argv[1].count("z")):
            print("z", end="")
    else:
        print("NONE")
else:
    print("NONE")