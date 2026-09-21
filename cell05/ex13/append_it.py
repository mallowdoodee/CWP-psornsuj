import sys

if len(sys.argv) >= 2:
    for each in sys.argv[1:]:
        if each.endswith("ism"):
            print(each)
        else:
            print(each + "ism")
else:
    print("NONE")