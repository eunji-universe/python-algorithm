'''
n*n의 격자판
각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력
각 자연수는 100을 넘지 않음
'''
import sys
# sys.stdin = open("input.txt", 'rt')

n = int(input())
bingo = [list(map(int, input().split())) for _ in range(n)]
largest = 0

# 각 행과 열의 합
for i in range(n):
    sum_row = sum_column = 0
    for j in range(n):
        sum_row += bingo[i][j]
        sum_column += bingo[j][i]
    if sum_row > largest:
        largest = sum_row
    if sum_column > largest:
        largest = sum_column

# 두 대각선
sum_diagonal_right = sum_diagonal_left = 0
for i in range(n):
    sum_diagonal_left += bingo[i][i]
    sum_diagonal_right += bingo[i][n-i-1]

if sum_diagonal_left > largest:
    largest = sum_diagonal_left
if sum_diagonal_right > largest:
    largest = sum_diagonal_right

print(largest)
