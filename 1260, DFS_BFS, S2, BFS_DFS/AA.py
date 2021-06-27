"""price =  [13, 15, 20, 100]
cost = [13, 15, 15, 0]

def solution(price, cost):
    price_maxx = 0
    sales_maxx = 0
    for price in prices:
        sales = sum([price-y for x, y in zip(prices, costs) if (x >= price) and (price > y)])


        if sales_maxx < sales:
            sales_maxx = sales
            price_maxx = price

    return price_maxx if price_maxx > 0 else 0

print(solution(prices = price, costs = cost))"""

X = 0
Y = 0
walkTime = 12
sneakTime = 25
min_time = 21470000

def dja(time, y, x):
    global X, Y, min_time
    if x == X and y == Y:
        if time < min_time:
            min_time = time
        return

    if sneakTime > 2 * walkTime:
        time = X * walkTime + Y * walkTime
        if time < min_time:
            min_time = time
    elif sneakTime < walkTime:
        pass
    elif sneakTime <= 2 * walkTime:
        time = min(X, Y) * sneakTime + abs(Y-X) * walkTime
        if time < min_time:
            min_time = time


dja(0, 0, 0)


print(min_time)
"""
문제 3
문제 설명
엘보니아의 왕은 int width미터 * int length미터 넓이의 궁전에서 살고 있다. 그는 신하들을 진흙 위에 살고 있게 하였기 때문에 인기 있는 왕은 아니었다. 그는 방문자들이 그를 접견하기 위해 오래 걷게 만들고 싶어서 궁전을 나누고 싶어했다. 왕의 보안 고문은 나선형으로 나누자고 제안했다. 방문자는 남서쪽 모서리에서 입궁하여 동쪽으로 걷는다. 방문자 앞에 벽이 나타나면 왼쪽으로 방향을 바꾼다. 나선형 복도의 너비는 1미터이다.

아래 다이어그램은 나선형 길의 한 예제이다:
방문객은 a (남서쪽 모서리)에서 출발하여 알파벳 순서대로 x (왕좌)까지 이동한다.
nmlkji
oxwvuh
pqrstg
abcdef

왕은 궁전의 길을 새로 만들기 전에 그의 왕좌를 먼저 정확한 위치로 옮기고 싶어하기 때문에 나선형의 길이 어디서 끝날지 알아야 한다. 왕좌의 좌표를 두개의 정수로 리턴하시오.

남서쪽 모서리는 (0, 0)이고 남동쪽 모서리는 (width - 1, 0), 그리고 북동쪽 모서리는 (width - 1, length - 1)이다.

참고 / 제약 사항
width와 length는 둘 다 최소값 1, 최대값 5000의 범위를 가진다.
테스트 케이스
int width = 6
int length = 4리턴(정답): [1,2]
문제 내용에 언급된 예제이다.

int width = 6
int length = 5리턴(정답): [3,2]
int width = 1
int length = 11리턴(정답): [0,10]
int width = 12
int length = 50리턴(정답): [5,6]
int width = 50
int length = 50리턴(정답): [24,25]"""

"""
문제 2
문제 설명
당신은 학교에서 집까지 도시를 거쳐 걸어가고 있다. 도시는 무한히 크며 모든 X값에는 수직 도로가 놓여있고 모든 Y에는 수평 도로가 놓여있다. 당신은 현재 (0, 0)에 있으며 (X, Y)에 있는 집에 가려고 한다. 집까지 가는 방법에는 두가지가 있다: 수평 혹은 수직으로 인접한 교차로를 거쳐 ( walkTime 초가 걸린다) 도로를 따라 걷는 것과 몰래 대각선으로 건너 ( sneakTime 초가 걸린다) 반대쪽 모서리로 가는 방법이 있다. 이미지에 나와있는 것처럼 걷거나 대각선을 가로지르는 8가지 방향 어느쪽으로도 가는 것이 가능하다 (예제 2번 참고).



집에 도착할 수 있는 최단 시간을 반환하여라. 명확한 이해를 위해 예제를 참고하여라.

참고 / 제약 사항
X는 0 이상, 1,000,000,000 이하이다.
Y는 0 이상, 1,000,000,000 이하이다.
walkTime은 1 이상, 10000 이하이다.
sneakTime은 1 이상, 10000 이하이다.
테스트 케이스
X = 4
Y = 2
walkTime = 3
sneakTime = 10리턴(정답): 18
전혀 가로질러가지 않는 것이 가장 빠른 길이다.

X = 4
Y = 2
walkTime = 3
sneakTime = 5리턴(정답): 16
가장 빨리 가는 방법은 두번 가로질러서 가는 길로서 경로는 다음과 같다: (0,0)->(1,0)->(2,1)->(3,1)->(4,2). 도합 가로지르는데 10초가 걸리고 걷는데 6초가 걸린다.

X = 2
Y = 0
walkTime = 12
sneakTime = 10리턴(정답): 20
다음과 같은 경로를 택할 수 있다: (0,0)->(1,1)->(2,0).

X = 1000000
Y = 1000000
walkTime = 1000
sneakTime = 1000리턴(정답): 1000000000
X = 0
Y = 0
walkTime = 12
sneakTime = 25리턴(정답): 0"""

"""문제1 설명
당신은 새 물건을 판매하기에 앞서 어떻게 하면 매출을 극대화할 수 있는지 알고 싶다. 물건의 최적의 가격을 정하는 것도 여러 전략 중 하나이다. 당신은 잠재적 고객들이 지출할 수 있는 제일 높은 가격을 적은 고객 목록을 만들었다. 당신은 또한 각 고객들에게 물건을 배송하기 위해 얼마의 비용이 필요한지 알고 있다. 배송 비용은 당신이 모두 부담해야되기 때문에 배송 비용이 너무 비싸다면 그 고객에게는 물건을 팔지 않을 수도 있다.

주어진 정수배열 price과 cost에는 각각 고객 i가 지출할 수 있는 제일 높은 가격과 배송 비용이 담겨 있다. 매출을 극대화할 수 있는 물건의 가격을 반환하여라. 최적의 가격이 2가지 이상 존재한다면 더 작은 가격을 리턴하시오. 이윤을 남길 수 없다면 0을 리턴하시오.

참고 / 제약 사항
price는 1개 이상, 50개 이하의 요소를 가지고 있다.
price의 각 요소는 1 이상, 10^6 이하이다.
cost는 price와 동일한 개수의 요소를 가지고 있다.
cost의 각 요소는 0 이상, 10^6 이하이다.
테스트 케이스
price = [13,22,35]
cost = [0,0,0]리턴(정답): 22
13원에 물건을 팔면 3명 모두 구입할 것이다: 매출: 3*13=39 22원에 물건을 팔면 2명만 구입할 것이다: 매출: 2*22=44 35원에 물건을 팔면 1명만 구입할 것이다: 매출: 1*35=35 그러므로 22가 최적의 가격이다.

price = [13,22,35]
cost = [5,15,30]리턴(정답): 13
13원에 물건을 팔면 3명 모두 구입하겠지만, 배송비를 고려하여 첫번째 고객에게만 물건을 팔 것이다: 매출: 13-5=8 22원에 물건을 팔면 2명이 구입하겠지만 배송비를 고려하여 두번째 고객에게만 물건을 팔 것이다: 매출: 22-15=7 35원에 물건을 팔면 1명만이 물건을 구입할 것이다: 매출: 35-30=5 그러므로 13이 최적의 가격이다.

price = [13,22,35]
cost = [15,30,40]리턴(정답): 0
배송비가 너무 비싸 누구에게도 팔 수 없으므로 0을 반환한다.

price = [10,10,20,20,5]
cost = [1,5,11,15,0]리턴(정답): 10
10원에 물건을 팔면 첫번째, 두번째 고객에게 물건을 팔고 14의 총 매출을 거둘 수 잇다. 20원에 물건을 팔면 세번째, 네번째 고객에세 물건을 팔고 14의 총 매출을 거둘 수 있다. 5원에 물건을 팔면 다섯번째 고객에게 물건을 팔고 5의 총 매출을 거둘 수 있다. 10과 20이 최적의 가격이므로 이 중에서 더 작은 10을 반환한다.

price = [13,17,14,30,19,17,55,16]
cost = [12,1,5,10,3,2,40,19]리턴(정답): 17"""

"""
4/5 가방 퀴즈
시간 제한 : 2초메모리 제한 : 256MB
문제 설명
1부터 n까지 번호가 붙여진 n개의 가방이 있다. 각 가방은 다른 가방에 넣을 수 있으며, 다른 가방에 들어간 가방 역시 다른 가방을 넣고 있을 수 있다. 문제의 명확성을 위해 가방 i가 가방 j의 안에 있다는 것은 가방 i가 가방 j에 직접적으로 들어있음을 의미한다.
예를 들어서, 가방 2가 가방 1 안에 있고, 가방 3이 가방 2 안에 있으면, 가방 3은 가방 2 안에 있지만 가방 1 안에 있지는 않다.

모든 가방은 처음에 다 빈 채로 바닥에 놓여 있다. 우리는 다음에 나열되는 것들 중 하나의 행동을 각각 단계적으로 취할 것이다.

PUT i INSIDE j - 가방 i를 가방 j안에 넣는다. 이 행동을 취하기 위해서는 가방 i와 j는 반드시 바닥에 놓여있어야 한다.
SET i LOOSE - 가방 i안에 있는 모든 가방을 다시 꺼내서 바닥에 놓는다. 이 행동을 취하기 위해서는 가방 i는 반드시 바닥에 놓여 있어야 한다.
SWAP i WITH j - 가방 i와 가방 j의 내용물을 서로 바꾼다 (다시 말하면, 가방 i의 모든 내용물을 꺼내서 가방 j에 넣고, 가방 j의 모든 내용물을 꺼내서 가방 i에 넣는다). 이 행동을 취하기 위해서는 가방 i와 j는 반드시 바닥에 놓여 있어야 한다.

가방들이 놓여진 마지막 상태에서 어떤 가방도 자기보다 더 작은 번호의 가방 안에 들어가 있지 않을 때, 이 상태를 적절하다고 말한다. 주어진 가방의 개수 int n과 취할 행동의 단계 vector<string> actions를 이용하여 마지막 상태가 적절한지 판단하여라. 만약 적절하다면 마지막 상태에 바닥에 놓인 가방의 개수를 반환하여라. 적절하지 않거나 어느 단계의 행동이 유효하지 않다면 -1을 반환하여라.

참고 / 제약 사항
n은 1 이상, 50 이하이다.
actions는 0개 이상, 50개 이하의 요소를 가진다.
actions의 각 요소는 "PUT i INSIDE j" (이 때, i와 j는 1부터 n사이의 서로 다른 두 정수이며 leading zero는 없다), 혹은 "SET i LOOSE" (이 때, i는 1부터 n사이의 정수이며 leading zero는 없다), 혹은 "SWAP i WITH j" (이 때, i와 j는 1부터 n사이의 서로 다른 두 정수이며 leading zero는 없다)와 같은 형태로 이루어지며 따옴표는 문자열에 포함되지 않는다.
테스트 케이스
int n = 2
vector<string> actions = ["PUT 1 INSIDE 2"]리턴(정답): 1
가방 1이 가방 2 안에 들어가 있으므로 적절한 상태이고 오직 하나의 가방만이 바닥에 놓여있다.

int n = 2
vector<string> actions = ["PUT 1 INSIDE 2","SET 2 LOOSE"]리턴(정답): 2
처음 상태와 마지막 상태가 동일하게 된다.

int n = 2
vector<string> actions = ["PUT 2 INSIDE 1"]리턴(정답): -1
가방 2가 가방 1 안에 들어가 있으므로, 더 적은 숫자의 가방 안에 들어가 있게 된다. 따라서 이 경우는 부적절한 상태이다.

int n = 4
vector<string> actions = ["PUT 3 INSIDE 2","SWAP 4 WITH 2","PUT 2 INSIDE 4","SET 1 LOOSE"]리턴(정답): 2
int n = 3
vector<string> actions = ["PUT 1 INSIDE 2","PUT 3 INSIDE 1"]리턴(정답): -1
마지막 행동은 가방 1이 바닥에 놓여 있지 않으므로 유효하지 않다."""

"""
5/5 도로 건설
시간 제한 : 2초메모리 제한 : 256MB
문제 설명
오늘 시의회 회의에서 전문가들이 도시 내에 늘어나는 교통량에 대해 경고했다. 아마도 타조 협회에서 타조들의 대규모 이동 때문에 도시로 접근하는 도로를 차단한 것이 원인인 것 같았다. 불행히도 이 때문에 많은 차들이 고속도로에서 빠져나오지를 못하고 있다. 공사 인부들이 비상 대피로를 만들어 차들이 빠져나갈 수 있도록 하고 있지만 차가 빠져나가는 규칙이 없다면 혼란에 빠질 것이다. 편안히 운전할 수 있도록 돕기 위해서 다음과 같은 규칙을 실시하기로 했다:

같은 도로 상에서 앞에 차가 있다면 빠져나갈 수 없다.
낮은 차선에서 차가 빠져나가려고 하는 경우 빠져나갈 수 없다.
차가 가장 앞에 도착했을 때 높은 차선에 있는 차에게 (가능하다면) 정확히 한번 양보해야 한다. 이는 (만약 더 높은 차선에 차가 있다면) 더 높은 차선에 있는 차가 먼저 빠져나가도록 하는 것을 의미한다.

위의 조건을 모두 충족시켰다면, 차는 고속도로에서 빠져나갈 수 있다. 그 후에 같은 도로에 있는 뒤차가 (현재 차가 마지막 차가 아니라면) 도로의 가장 앞으로 나온다.
예를 들어서, 도로에 아래와 같이 다섯 개의 차량이 있다고 가정하자 (왼쪽이 차선의 가장 앞이다):
0 A B
1 C D
2 E
A 차는 아직 양보하지 않았으며 먼저 양보해야 한다. C 차 역시 마찬가지이다. 더 높은 차선이 없는 E 차는 양보할 수 없으므로 먼저 빠져나간다. A 차는 한번 양보했으므로 빠져나갈 수 있다. B 차가 앞쪽으로 이동하지만 아직 양보하지 않았기 때문에 먼저 C 차에게 양보해야 한다. C 차가 빠져나가고 나서 B 차가 빠져나간다. 마지막으로 D 차가 빠져나간다.

문제에서는 vector<string> currentLanes가 주어진다. vector<string> currentLanes의 i번째 요소는 i차선에 있는 차들을 의미한다. 0번째 요소는 차선 가장 앞 쪽에 있는 차를 의미한다. vector<string> currentLanes에 있는 어떠한 차도 아직 다른 차에게 양보하지 않았다. 'D'로 표시된 차를 멀리서 온 다른 나라의 외교관이다. 외교관이 도착하기 전까지 얼마만큼의 시간이 남았는지 알기 위해서 외교관이 빠져나오기 위해서 몇 대의 차량이 먼저 빠져나가야 하는지 알고 싶다. 이 숫자를 반환하여라.

참고 / 제약 사항
currentLanes는 최소 1개, 최대 50개의 요소를 가지고 있다.
currentLanes의 각 요소는 최소 1개, 최대 50개의 문자를 가지고 있다.
currentlanes의 각 문자는 대문자이다 ('A'-'Z').
currentLanes에는 오직 한 개의 'D'가 있다.
테스트 케이스
vector<string> currentLanes = ["AB","CD","E"]리턴(정답): 4
문제 내용에 나온 예제이다.

vector<string> currentLanes = ["AH","D","BCG","E","F"]리턴(정답): 2
F 차가 먼저 빠져나가고 나서 A 차가 빠져나간다. 그리고 나면 D 차가 빠져나갈 수 있다.

vector<string> currentLanes = ["ABC","DEF"]리턴(정답): 0
하나의 알파벳으로 여러 개의 차량이 표현될 수 있다. 하지만 D는 오직 하나 뿐이다.

vector<string> currentLanes = ["ABEDSCSMAN"]리턴(정답): 3
vector<string> currentLanes = ["AAA","A","AAA","A","AAD","A","AAB"]리턴(정답): 13
"""

dja(0, 0, 0)
print(min_time)

def solution(X, Y, walkTime, sneakTime):

    return 0
