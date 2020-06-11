'''
앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점
연속해서 답이 맞는 경우 k번째 문제는 k점
틀린 문제는 0점
n개의 문제에 대해 답이 맞은 경우 1, 틀린 경우 0으로 표시하였을 때 점수 계산
'''
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
scores = list(map(int, input().split()))

sum = 0
cnt = 0
for score in scores:
    if score == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)