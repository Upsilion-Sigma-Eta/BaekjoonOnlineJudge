X = int(input())
for _ in range(int(input())):
    price, quantity = map(int, input().strip().split())
    X -= price * quantity

if (X == 0):
    print("Yes")
else:
    print("No")