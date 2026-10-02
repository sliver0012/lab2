n = int(input())

first = n // 10
second = n % 10

if first > second:
    print(1)
elif second > first:
    print(2)
else:
    print("=")