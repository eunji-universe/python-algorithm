'''
n개의 수로 된 수열 
이 수열의 i번째 수부터 j번째 수까지의 합이 m이 되는 경우의 수 구하는 프로그램
수열에 들어가는 값은 자연수
'''
import sys
# sys.stdin = open("input.txt", 'r')
n, m=map(int, input().split())
nums = list(map(int, input().split()))
lt = 0
rt = 1
tot = nums[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += nums[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= nums[lt]
        lt += 1
    else:
        tot -= nums[lt]
        lt += 1
print(cnt)