def solution():
    n, m = map(int, input().split())
    count = 0

    while True:
        target = (n//m) * m
        count += n-target
        n = target

        if n < m:
            break
        n //= m
        count += 1

    count += (n-1)

    return count

print(solution())
