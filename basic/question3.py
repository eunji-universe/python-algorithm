'''
1부터 100까지의 자연수가 적힌 N장의 카드 중 3장을 뽑아 값을 합한다. 
3장을 뽑을 수 있는 모든 경우를 기록했을 때
기록한 값 중 k번째로 큰 수를 출력. (중복된 수 주의)
'''

import sys
# sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
num = list(map(int, input().split()))
result = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
           result.add(num[i] + num[j] + num[m])

result = list(result)
result.sort(reverse = True)
print(result[k-1])
