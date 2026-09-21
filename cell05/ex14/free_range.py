import sys
arr = []
if len(sys.argv) >= 3:
    for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
        arr.append(i)
    print(arr)
else:
    print("NONE")