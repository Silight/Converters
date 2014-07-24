# Fehrenheit to Celsius 
# (°F  -  32)  x  5/9 = °C

fString = input("Enter temperature in Fehrenheit: ")
f = float(fString)
c = (f - 32) * (5 / 9)
print("The temperature in Celsius: " + str(c))
