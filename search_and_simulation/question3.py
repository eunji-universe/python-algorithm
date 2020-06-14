'''
한국정보올림피아드 문제
카드 역배치
'''
import sys
# sys.stdin = open("input.txt", "rt")

cards = list(range(21))

for _ in range(10):
    start, end = map(int, input().split())
    for i in range((end - start + 1) // 2):
        cards[start+i], cards[end-i] = cards[end-i], cards[start+i]

cards.pop(0)
for card in cards:
    print(card, end=' ')