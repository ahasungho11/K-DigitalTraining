# --------------------------------------------------------------------------------------------------
# 파이썬에서 미리 만들어서 제공하는 클래스
# int, float, bool, str, list, tuple, dict, set
# --------------------------------------------------------------------------------------------------
num=123       # 실제로는 int() 생성자 실행된 것
num2=int(123) # 원래 이렇게 써야하지만, 이미 만들어져 있는 것을 쓰므로 
abc=10.3         # 실제로는 float() 생성자 실행된 것
abc=float(10.3)  # 원래 이렇게 써야하지만, 이미 만들어져 있는 것을 쓰므로
print(num, num2)

# 이처럼 자동차를 입력할 수 있는 클래스를 만들어야 함

abc=10.3
abc=float(10.3)
carNum = int(1234)
carBrand = 'Hyundae'

#이런 것들을 다 만들수 있는 datat type을 만들어야 함

# ex) class Car:


## 내가 만드는 class -> 평면에 좌표값을 저장하는 데이터
# 클래스명 : Point
# 속성/특징/변수 : x, y (포인트를 만들려면 필요한 2가지 라는 것)
# 역할/기능/함수 :
# - Point 클래스로 메모리에 존재하는 객체(인스턴스)를 생성하는 메서드가 있어야 함  __init__(self, x, y)
# - 객체 안만들 것 같으면 클래스를 굳이 만들필요는 있을까(함수만 들어가는 메서드가 있긴함
# - 인스턴스의 값을 읽어주는 메서드 -> get속성명() -> 메모리에 들어있는 현재 속성값 반환
# - 객체(인스턴스)에 값을 변경해주는 메서드 -> set속성명(새로운값)
# - 내가 원하는 기능 메서드

# ex) class _Support~ : 클래스 감추는 기능 => '_'

# object : 모든 클래스의 조상
# _init__ : 모든 오브젝트를 상속 받을 수 있음

#-------------

# ()가 없으면 무조건 상속 받는 다는 것
# ex) class int
######
### Class Point:
    #Point 인스턴스를 생성하는 메서드

class Point:
    def __init__ (self, x, y):
        self._x = x
        # self.__x = x (한번 넣으면 바꿀 수 없게끔 '__'입력, 외부에서 직접 접근 못하게 하기 위해 => getter 속성 써야)
        self.y = y

# getter와 setter 메서드는 선택사항
# Point 인스턴스에 저장될 속성(변수)값 읽어오는 메서드 -> getter메서드
    def getX(self): return self._x
    def getY(self): return self.y
    def getXY(self): return self.x, self.y

# Point 인스턴스에 저장된 속성(변수)값 저장하는 메서드 -> setter메서드
    def setX(self, x): self._x=x
    def setY(self, y): self.y=y
    def sefXY(self, x, y): self.x, self.y

#-------------------------------------------
# Point 인스턴스 중 객체 생성 하기
p1.Point(10,5)
#
# p1.set(5)
# print(p1.getx(), p1.x)
#
# p1.x = 1000
# print(p1.getx(), p1.x)

#--------------------------------------------
    # 내가 원하는 기능의 메서드
    # Point 인스턴스와 정보 출력되는 메서드(Method)
    def showPoint(self):
        print(f'현재 좌표값 ({self.x}, {self.y}')

    def drowPoint(self):
    # Point 인스턴스에 해당하는 좌표를 그리는 메서드
    # x값은 가로로 이동
    # y값은 다음줄 \n
        print('\n' * self.y, end='')
        print(' ' * self._x * '★' , end='')

#-----------------------------------------------------------------------------------
p1.Point(10,2)
p1.drowPoint()

nums=[1,4,5,2,2,5,8,2]      # 인트 객체들이 들어 있는 것
points=[Point(10,10), Point(3,4), Point(4,2), Point(0,0)]    # 포인트 객체들이 들어 있는 것

# 리스트에 객체들 다 집어 넣고
# 필요한 요소만 바꿔가면서 입력하고 출력하면
# 각 객체 다 생성할 필요 없음

