'''
n개의 문자열 데이터를 입력받아
회문 문자열이면 YES 출력, 아니면 NO 출력.
대소문자 구분 안 함
'''
import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())
for i in range(n):
    word = input()
    word = word.lower()

    # 방법 1
    # size = len(word)
    # for j in range(size//2):
    #     if word[j] != word[-1-j]:
    #         print(f"#{i+1} NO")
    #         break
    # else:
    #     print(f"#{i+1} YES")



    # 방법 2
    if word == word[::-1]:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")