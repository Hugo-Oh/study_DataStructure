"""1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게
임이 있다.
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된
다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금
으로 받게 된다.
N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램
을 작성하시오"""

"""
3
6 2 5
3 3 6
2 2 2

12000
"""
# list + len으로 할까? 으로 일단 눈 세개 입력
# 경우의수는 len이 1 / len 2 / len 3
# 그 다음에 나온 len이 이전 len보다 크면 체인지 같으면 비교 등등..

N = int(input())
price = []
for _ in range(N):
    arr = list(map(int, input().split()))
    if len(set(arr)) == 1:
        price.append(10000 + sorted(arr)[1] * 1000)
    elif len(set(arr)) == 2:
        price.append(1000 + (sorted(arr)[1] * 100))
    else:
        price.append(max(arr) * 100)

print(max(price))


