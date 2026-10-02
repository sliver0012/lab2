n = input("Enter a three-digit number: ").strip()

a = int(n[0])
b = int(n[1])
c = int(n[2])

maxd = max(a, b, c)
mind = min(a, b, c)

if maxd == mind:
    print(maxd)
else:
    print(f"{maxd} {mind}")