
a = []
c = 1
def main():
    global a
    n = int(input("num: "))
    size = 2**n
    a = [[0] * size for i in range(size)]
    solve(0, 0, n)
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print("")

def solve(px, py, n):
    global c
    if n == 0:
        a[px][py] = c
        c += 1
        return
    solve(px, py, n-1)
    solve(px, py + 2**(n-1), n-1)
    solve(px + 2**(n-1), py, n-1)
    solve(px + 2**(n-1), py + 2**(n-1), n-1)
    return

main()