'''
두 개의 정 n면체와 정 m면체의 주사위를 던져서 나올 수 있는 눈의 합 중
가장 확률이 높은 숫자를 출력하는 프로그램.
정답이 여러 개일 경우 오름차순으로 출력
'''

import sys
# sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
cnt = [0]*(n+m+1)
max = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in range(len(cnt)):
    if cnt[i] > max:
        max = cnt[i]

for i in range(len(cnt)):
    if cnt[i] == max:
        print(i, end=' ')