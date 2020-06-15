'''
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램
n, m: 리스트의 크기
'''
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
p1 = p2 = 0
result = list()

while p1 < n and p2 < m:
    if list1[p1] <= list2[p2]:
        result.append(list1[p1])
        p1 += 1
    else:
        result.append(list2[p2])
        p2 += 1
if p1 < n:
    result += list1[p1:]
else:
    result += list2[p2:]


for x in result:
    print(x, end=' ')