def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 8
    if n > 4:
        return f(n-1) + f(n-2) + f(n-3) + f(n - 4)

print(f(12))
