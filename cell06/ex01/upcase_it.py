import sys

def upcase_it(text):
    return text.upper()

for arg in sys.argv[1:]:
    print(upcase_it(arg))