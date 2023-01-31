# A non-empty array A consisting of N integers is given.
# The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value,
# except for one element that is left unpaired.
#
# For example, in array A such that:
#
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the elements at indexes 0 and 2 have value 9,
# the elements at indexes 1 and 3 have value 3,
# the elements at indexes 4 and 6 have value 9,
# the element at index 5 has value 7 and is unpaired.
# Write a function:
#
# def solution(A)
#
# that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
#
# For example, given array A such that:
#
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the function should return 7, as explained in the example above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.
# Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

def solution(A): #O(N) or O(N*log(N))의 시간 복잡도
    # 중복제거를 위해 비트연산을 해줍니다.
    # X ^ (Y ^ Z) = (X ^ Y) ^ Z : 연산의 순서를 바꿔도 결과가 같다
    # X ^ X = 0 ,  0 ^ X = X, 0 ^ 0 = 0: 연산하는 두 수가 같으면 0, 0과 다른 수를 연산하면 그 수가 결과로 나온다.
    # 문제에서 항상 홀수 개의 원소가 주어지고, 쌍이 없는 원소는 단 하나라 했기에 가능한 풀이 입니다.
    x = 0
    for number in A:
        x ^= number
    return x

from heapq import heapify, heappop, heappush
def solution2(A):
    answer = []
    heapify(A)
    while True:
        if len(A) > 1:
            if A[0] == A[1]:
                heappop(A) # heappop을 쓰면 heap의 순서가 오름차순이 아니게 되어 의도하지 않은 원소를 삭제하게 됩니다. 오답.
                heappop(A) # 그래서 지우고 다시 정렬하고 지우고 다시 정렬하는 식으로 하면 큰 수의 길이에 대해서 시간초과가 납니다.
            else:
                heappush(answer, A[0])
                heappop(A)
        elif len(A) == 1:
            heappush(answer, A[0])
            break;
        else:
            break;
    return answer[0]

def solution3(A): #O(N**2) 의 시간 복잡도를 가지는데 범위로 주어진 A의 길이가 길어지면 시간초과 문제가 생깁니다.
    A.sort()
    answer = []
    while True:
        if len(A) > 1:
            if A[0] == A[1]:
                del A[0]
                del A[0]
            else:
                answer.append(A[0])
                del A[0]
        elif len(A) == 1:
            answer.append(A[0])
            break;
        else:
            break;
    return answer[0]

A = [9 ,3 ,9 ,3 ,9 ,7, 9]
print(solution(A))

A = [9 ,3 ,9 ,3 ,9 ,7, 9]
print(solution2(A))

A = [9 ,3 ,9 ,3 ,9 ,7, 9]
print(solution3(A))