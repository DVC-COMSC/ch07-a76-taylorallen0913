
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

merged = []

if len(num1) == len(num2) or len(num1) < len(num2):
    merged = num1 + num2
else:
    merged = num2 + num1


print(merged)