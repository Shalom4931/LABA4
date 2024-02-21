import random
def gener(n):
    for i in range(n):
        yield i*i

numbers = gener(int(input("Number: ")))
for j in numbers:
    print(j)    