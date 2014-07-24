# Finds the area of a trapazoid
# a = (x + y) / 2 * h

print("Area of a trapezoid")
hString = input("Enter the height of the trapezoid: ")
xString = input("Enter the length of the bottom base: ")
yString = input("Enter the length of the top base: ")
h = float(hString)
x = float(xString)
y = float(yString)
a = (x + y) / 2 * h
area = str(a)
print("The area is: " + area)