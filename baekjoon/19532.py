a, b, c, d, e, f = map(int, input().split())
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a * i + b * j == c:
            if d * i + e * j == f:
                if (a - d) * i + (b - e) * j == c - f:
                    print(i, j)