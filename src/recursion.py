def fat(n):
    if n == 1:
        return 0
    else:
        return n + fat(n - 1)

