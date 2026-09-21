import sys
# print("Number of parameters: {}.".format(len(sys.argv) - 1))
if len(sys.argv) <= 2:
    print("None")
else:
    for arg in reversed(sys.argv[1:]): print(arg.lower())