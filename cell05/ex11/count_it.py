import sys

if len(sys.argv) > 2:
    print(f"parameters: {len(sys.argv)-1}")
    for each in sys.argv[1:]:
        print(f"{each}: {len(each)}")
else:
    print("NONE")
