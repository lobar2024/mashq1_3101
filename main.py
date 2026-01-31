a = list(map(int, input().split()))
juftlar = []

for x in a:
    if x % 2 == 0:
        juftlar.append(x)

print(max(juftlar))
