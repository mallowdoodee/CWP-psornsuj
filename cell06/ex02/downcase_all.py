import sys
def upcase_it(text):
    return text.lower()

if len(sys.argv) > 2:
    for each in sys.argv:
        print(upcase_it(each))
else:
    print("none")