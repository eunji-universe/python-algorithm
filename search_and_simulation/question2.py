'''
문자와 숫자가 섞여있는 문자열이 주어지면
그 중 숫자만 추출하여
그 순서대로 자연수를 만들고
만들어진 자연수와 그 자연수의 약수의 개수를 출력
'''
import sys
# sys.stdin = open("input.txt", "rt")

datas = input()

num = 0
for data in datas:
    if data.isdecimal():
        num = (num * 10) + int(data)
print(num)


cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1
print(cnt)