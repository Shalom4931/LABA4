def gen(n):
    for i in range(n, -1, -1):
        yield i

numbers = gen(int(input("number: ")))
for j in numbers:
    print(j)