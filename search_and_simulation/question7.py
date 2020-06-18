'''
n은 항상 홀수
각 자연수는 사과나무에 열린 사과의 개수
다이아몬드 모양의 격자판만 수확
수확하는 사과의 총 개수 출력
'''
import sys
# sys.stdin = open("input.txt", 'rt')

n = int(input())
apples = [list(map(int, input().split())) for _ in range(n)]

res = 0
start = end = n // 2
for i in range(n):
    for j in range(start, end + 1):
        res += apples[i][j]
    if i < n//2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1
print(res)