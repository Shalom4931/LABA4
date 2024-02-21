def squares(a,b):
    for i in range(a,b+1):
        yield i*i

numbers = squares(int(input("a: ")), int(input("b: ")))
for j in numbers:
    print(j)