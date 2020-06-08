'''
1부터 n까지의 자연수 중 소수의 개수를 출력
'''
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())

nums = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if nums[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            nums[j] = 1

print(cnt)
        