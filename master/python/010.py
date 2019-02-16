'''
저는 카카오에 주식을 1000주 보유하고 있습니다. 현재 카카오의 주가는 10만원 이에요. 제가 보유하고 있는 재산을 계산하는 함수를 만들어 주세요.
input : 1000, 100000
output: 1억
'''
kakaostock = int(input('주식수를 입력하세요:'))
kakaoprice = int(input('주가를 입력하세요'))
def kakao(a, b):
    return a * b
print(kakao(kakaostock, kakaoprice))

def kakaotwo():
    #인자값으로 전달하지 않아도 안에서 밖을 보는 것은 허용
    return kakaostock * kakaoprice
print(kakaotwo())



    