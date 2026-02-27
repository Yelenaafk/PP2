import math

# 1. Convert degree to radian
degree = 15
radian = math.radians(degree)

print("Degree:", degree)
print("Output radian:", round(radian, 6))


# 2. Area of a trapezoid
height = 5
base1 = 5
base2 = 6

trapezoid_area = (height * (base1 + base2)) / 2

print("\nHeight:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", trapezoid_area)


# 3. Area of regular polygon
n = 4
side = 25

polygon_area = (n * side**2) / (4 * math.tan(math.pi / n))

print("\nInput number of sides:", n)
print("Input the length of a side:", side)
print("The area of the polygon is:", int(polygon_area))


# 4. Area of a parallelogram
base = 5
height_parallelogram = 6

parallelogram_area = base * height_parallelogram

print("\nLength of base:", base)
print("Height of parallelogram:", height_parallelogram)
print("Expected Output:", float(parallelogram_area))