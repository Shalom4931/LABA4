from math import tan, pi

def pol(n, s):
    area = (n * s**2) / (4 * tan(pi / n))
    return area

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = pol(n, s)
print("The area of the polygon is:", area)