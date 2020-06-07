'''
n개의 자연수 입력
각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력.
각 자연수의 자릿수의 합을 구하는 함수 def digit_sum(x)를 작성하여 프로그래밍 할 것
'''
import sys
# sys.stdin = open("input.txt", "rt")

def digit_sum(x):
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])   
    return sum

n = int(input())
nums = input().split()

max = -1

for num in nums:
    sum = digit_sum(num)
    if sum > max:
        max = sum
        result = num

print(result)

