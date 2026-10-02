circle=float(input("Enter the radius of the circle: "))
square=float(input("Enter the side length of the square: "))

areacircle=3.14*circle**2
areasquare=square**2

if areacircle>areasquare:
    print("circle")
elif areacircle<areasquare:
    print("square")