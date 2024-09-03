from math import pi, sqrt as sq, cos, sin, e, pow, exp

#in class examples

print(f"{pi:.2f}") #format specifier to display only 2 decimal places

for x in range (1, 11):
    print(f'{x:2} {x**2:3} {x**3:4}')

try:
    radius = int(input("Give me the radius: "))
    area = (pi * radius ** 2)
    print(sq(area))
    print(area)
except Exception as e:
    print("Please enter valid number next time.")


#exercises from Ch2

#Part 1
radius = 5
volume = ((4 / 3) * pi * radius**3)
print('volume =' , volume)
# radius in centimeters, volume in cubic centimeters

#Part 2
x = 42
c = (cos(x))**2
s = (sin(x))**2
print(c + s)

#Part 3
#three ways to square e

w1 = e**2
w2 = pow(e, 2)
w3 = exp(2)
print('natural logarithm', w1, w2, w3)

