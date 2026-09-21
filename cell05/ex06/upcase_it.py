import sys
# print("Number of parameters: {}.".format(len(sys.argv) - 1))
if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print("None")