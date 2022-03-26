try:
    x=int(input("X: "))
except:
    print("That is not an int!")
    exit()
try:
    y=int(input("Y: "))
except:
    print("That is not an int!")
    exit()

z=x/y
print(f"{z:.50f}")