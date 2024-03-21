# ex1
import math

degree = float(input("degree = "))
radian = degree * (math.pi / 180)
print("radian =", round(radian, 6))

# ex2 
height = float(input("height = "))
base1 = float(input("base1 = "))
base2 = float(input("base2 = "))

area = 0.5 * (base1 + base2) * height
print("area =", area)



# ex3
num_sides = int(input("number of sides = "))
side_length = float(input("length = "))

area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print("polygon area =", round(area, 2))



# ex4
base_length = float(input("base = "))
height = float(input("height = "))

area = base_length * height
print("area =", area)
