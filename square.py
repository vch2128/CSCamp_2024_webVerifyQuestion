x = int(input())

flag = False
for i in range(16):
    y = (i+1)**2 + (i+2)**2 + (i+3)**2
    if y == x:
        print("yes")
        flag = True
        break

if flag == False:
    print("no")