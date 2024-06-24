a = [0 for i in range(200)]
a[1] = 1
a[2] = 1

def main():
    x = int(input("輸入費波那契數列項數: "))
    print(fibonnaci(x))

def fibonnaci(x):
    if a[x] != 0:
        return a[x]
    if a[x - 1] == 0:
        a[x - 1] = fibonnaci(x-1)
    if a[x - 2] == 0:
        a[x - 2] = fibonnaci(x-2)
    a[x] = a[x-1] + a[x-2]
    return a[x]
    
main()