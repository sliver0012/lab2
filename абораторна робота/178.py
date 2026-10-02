t = int(input("Enter the time in minutes: "))

cycle = t % 5

if cycle < 3:
    print("green")
else:
    print("red")
