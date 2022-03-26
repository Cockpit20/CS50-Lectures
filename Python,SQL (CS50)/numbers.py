import sys

numbers = [4,6,8,5,7,2]
if 0 in numbers:
    print("Found")
    sys.exit(0)

print("Not Found")
sys.exit(1)
