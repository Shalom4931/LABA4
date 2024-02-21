def gen(n):
    for i in range(n):
        if i%12==0:
            yield i

numbers = gen(int(input("number: ")))
for j in numbers:
    print(j)