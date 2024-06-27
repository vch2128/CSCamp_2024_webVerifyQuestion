
def solve_task1(number):   # star_advance
    a = ""
    for i in range(number):
        for j in range(number-i-1):
            a += " "
        for j in range((i+1)*2 - 1):
            a += "*"
        a += '\n'
    a = a[:-1] # 把最後一個"\n"刪掉
    return a
x = int(input())
a = solve_task1(x)
print(a)
