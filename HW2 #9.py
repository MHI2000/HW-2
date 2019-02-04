import math
t =  (float(input("The temperature in Fahrenheit: ")))
v = (float(input("The wind speed in miles/hour: ")))



wci = 35.74 + (0.6215*t) - 35.75*(v**0.16) + 0.4275*t*(v**0.16)

print("The wind chill is ", int(round(wci, 0)))




