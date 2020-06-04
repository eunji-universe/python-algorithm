'''
n개의 숫자로 이루어진 숫자열에서 s번째부터 e번째 까지의 수 중 k번째로 작은 수 출력
'''

import sys
# sys.stdin = open("input.txt", "rt")
T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_list = num_list[s-1:e]
    num_list.sort()
    print(f"#{t+1} {num_list[k-1]}")