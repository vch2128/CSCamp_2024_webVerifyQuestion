x = int(input())

def f(x):
    if x%2 == 0:
        return f(x/2)
    elif x != 1:
        return f(x-1)+f(x+1)
    return 1

print(f(x))