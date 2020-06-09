'''
n개의 자연수 입력
각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 뒤집은 수를 출력
뒤집는 함수 reverse(x)
소수인지 확인하는 함수 isPrime(x)
'''
import sys
# sys.stdin = open("input.txt", "rt")

def reverse(x):
    result = 0
    while x > 0:
        n = x%10
        x = x//10
        result = result*10 + n
    return result
    
        

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, (x//2)+1):
        if x%i == 0:
            return False
    else:
        return True

n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    num = reverse(num)
    if isPrime(num):
        print(num, end=' ')

        