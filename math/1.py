from math import pi
def degrees(n):
    rad = n*(pi/180)
    return rad

degr = degrees(int(input("Input degree: ")))
res = degr
print(f"Output radian: {res}")