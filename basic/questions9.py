'''
n명이 주사위 3개를 던져서 다음 규칙에 따라 상금 받음
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
가장 많은 상금을 받는 사람의 상금을 출력
'''
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
result = 0
for i in range(n):
    dice = input().split()
    dice.sort()
    
    a, b, c = map(int, dice)

    if a == b == c:
        reward = 10000 + (a * 1000)
    elif a == b or a == c:
        reward = 1000 + (a * 100)
    elif b == c:  # reward 계산을  간단히 하기 위해 따로
        reward = 1000 + (b * 100)
    else:
        reward = c * 100
    
    if reward > result:
        result = reward

print(result)


        