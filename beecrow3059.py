res = 0

n, i, f = map(int, input().split())

v = list(map(int, input().split()))

for j in range(n):

    for k in range(j, n):

        if j != k and v[j] + v[k] >= i and v[j] + v[k] <= f:

            res += 1

print(res)
