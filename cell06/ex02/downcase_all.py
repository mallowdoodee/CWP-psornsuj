import sys
def downcase_it(text):
    return text.lower()

if len(sys.argv) > 2:
    for each in sys.argv:
        print(downcase_it(each))
else:
    print("none")

# python ./downcase_all.py "HELLO WORLD" "I understood Arrays well!"