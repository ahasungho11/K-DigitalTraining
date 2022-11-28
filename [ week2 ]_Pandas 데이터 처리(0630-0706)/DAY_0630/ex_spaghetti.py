# ----------------------------------------------------------------
# 알리오 올리오 만들기
# 속성/필드/변수 : 면, 소스, 채소 (공통)
# 기능/함수 : 물 끓이기, 면 삶기, 재료 손질하기, 볶기, 먹기 (함수)
# 기타재료 넣을 것이 있으면 따로 받아도 됨 (함수 정의 하는 지점의 파라미터에)

import time as t
# => 모듈을 import 할 때는 class 밖에서 해야

class Alio:

    def __init__(self, noodle, sauce, *vagetable):
        self.noodole = noodle
        self.sauce = sauce
        self.vegatable = vegetable

    # getter/setter 메서드 (선택)
    # def getData(self): return self.data
    # def setData(self, *data): self.data = data

    # 주문받기 - 조리시작 - 시식
    
    # 조리 시작 (물 끓이기, 면 삶기, 재료 손질하기, 볶기, 먹기)
    #          (면, 소스, 채소)

    pot = []  # 이렇게 쓰는게 맞는 건지
    pan = []

    def boil(self, pot, water):
        pot = water
        t.sleep(2)
        print('물이 끓고 있습니다')
        return water            # 면수

    def steam(self, pot):
        pot += self.noodle
        print('면을 삶고 있습니다.')
        t.sleep(2)
        print('면과 면수를 얻었습니다.')
        return pot       # 면

    def prepFry(self, pan, pot):
        pan += pot
        pan += self.vegatable[:]
        t.sleep(2)
        print('조리를 완료했습니다.') # 손질된 재료를 볶아

    def eating(self):
        print('주문하신 알리오 올리오 나왔습니다. 남기지 마세요')

#--------------------------------------------------------------------
cookMeal = Alio('면', '소스', '야채')

cookMeal.boil(pot, water)

# 함수에 적는 파라미터의 경우, 객체를 만들고 함수를 구동할 때 적는 파라미터

# 조리 과정 마무리
# 주문 받는 과정 추가