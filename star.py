x = int(input("列數："))

for i in range(x):
    for j in range(i + 1):
        print("*", end="")
    print("") 