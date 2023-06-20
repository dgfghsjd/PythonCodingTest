import time

def solution():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    # st = time.time()
    a = max(data)
    data.remove(max(data))
    b = max(data)

    # data.sort()
    # a = data[-1]
    # b = data[-2]
    # end = time.time()
    # print(end-st)
    # max를 두 번 찾는 방법이 sort한 후 마지막 두 개 찾는 것보다 빠르다.

    # num_of_b = m // (k+1)
    # num_of_a = m - num_of_b
    # answer = a * num_of_a + b * num_of_b
    # 위 풀이는 예쁜 예시 케이스만 풀 수 있다.
    result = 0
    while True:
        for i in range(k):
            if m == 0:
                break
            result += a
            m -= 1
        if m == 0:
            break
        result += b
        m -= 1

    return result

print(solution())