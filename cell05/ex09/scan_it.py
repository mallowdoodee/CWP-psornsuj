import sys
if len(sys.argv) <= 2:
    print("None")
else:
    print(sys.argv[2].count(sys.argv[1]))