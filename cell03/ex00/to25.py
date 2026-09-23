num = int(input("Enter num less than 25: "))
if num > 25:
    print(num, "Error.")
else:
    for i in range(num, 26):
        print("Inside the loop, my variable is", i)