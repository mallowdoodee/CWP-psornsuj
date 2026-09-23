import re
import sys
if len(sys.argv) <= 2:
    print("None")
else:
    print(len(re.findall(sys.argv[1], sys.argv[2])))

# ./scan_it.py "the" "the quick brown fox jumps over the lazy dog"
