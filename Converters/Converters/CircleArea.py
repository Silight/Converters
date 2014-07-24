# Finds the area of a Circle
# a = 3.14 * (r * r)

dString = input("Enter the diameter of the circle: ")
d = float(dString)
r = d / 2
a = 3.14 * (r * r)
area = str(a)
print("The area is: " + area)