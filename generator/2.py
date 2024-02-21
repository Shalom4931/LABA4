def gener(n):
    for i in range(n):
        if i%2==0:
            yield str(i)

numbers = gener(int(input("Number: ")))
res = ", ".join(numbers).rstrip(",")
print(res)