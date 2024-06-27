x = int(input())

left_apple = 500 % x
price = 30
money = 0
rate = 1
while left_apple > 0:
    current_apple = 0
    if left_apple >= 10:
        current_apple = 10
    else:
        current_apple = left_apple

    money += current_apple * price * rate
    
    rate -= 0.05
    left_apple -= current_apple

print(int(money))