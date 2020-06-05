'''
n명의 학생의 수학성적
평균(소수 첫째자리 반올림)을 구하고 
평균 점수와, n명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력.
답이 2개일 경우 성적이 높은 학생, 답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호를 답으로
'''

import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
grades = list(map(int, input().split()))

# 평균 구하기. round는 round_half_even 방식이므로 쓰지 말자
avg = int(sum(grades)/n + 0.5)

min_of_diff = 2147000000
for id, grade in enumerate(grades):
    temp = abs(avg - grade)
    if temp < min_of_diff:
        min_of_diff = temp
        result_id = id + 1
        result_grade = grade
    elif temp == min_of_diff:
        if result_grade < grade:
            result_id = id + 1
            result_grade = grade

print(avg, result_id)