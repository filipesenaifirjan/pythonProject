n = int(input())
rMax = -1
pMin = 0
for i in range(n):
    pg = list(map(float, input().split()))
    r = pg[1] / pg[0]
    if r > rMax:
        rMax = r
        pMin = 1000 / r

print("{:.2f}".format(pMin))
