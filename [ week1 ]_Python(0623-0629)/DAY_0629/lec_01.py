# ---------------------------------------------------
# 파이썬에서 미리 만들어서 제공하는 클래스
# int, float, bool, str, list, tuple, dict, set
# ---------------------------------------------------
num=123
num2=int(444)       # 미리 만들어서 주는.... 실제로는 int() 생성자 실행

name='Hong'
name=str('Hong')    # 실제로는 str() 생성자 실행
print()
# ---------------------------------------------------
# 내가 만드는 클래스 -> 평면에 좌표값을 저장하는 데이터
# 클래스명 : Point
# 속성/특징/변수 : x, y
# 역할/기능/함수
#   - Point 클래스로 메모리에 존재하는 객체(인스턴스) 생성하는 메서드 =>  __init__(self, s, y)
#   - 객체(인스턴스)에 값을 읽어주는 메서드   => get속성명() ---> 현재 속성값 반환
#   - 객체(인스턴스)에 값을 변경해주는 메서드 => set속성명(새로운값) ---> 반환값 없음
#   - 내가 원하는 기능 메서드로 만듦
# ---------------------------------------------------
class Point():
    # Point 인스턴스를 생성하는 메서드      생성자 메서드(컨스턴스 메서드)
    def __init__(self, x, y):
        self._x = x                # 언더바가 한개 혹은 두개 붙으면 클래스 밖에서는 볼 수 없다(수정 불가능), 프라이빗... 수정하려면 get set 메소드 생성
        self.y = y

    # # Point 인스턴스에 저장된 속성(변수)값 읽어오는 메서드 => getter메서드
    def getX(self): return self._x              # 한개 값 읽어오기
    # def getY(self): return self.y
    # def getXY(self): return self.x, self.y     # 두개 값 동시에 읽어오기
    #
    # # Point 인스턴스에 저장된 속성(변수)값 저장하는 메서드 => setter메서드
    def setX(self, x): self._x = x       # 한개 값 저장하기
    # def setY(self, y): self.y = y
    # def setXY(self, x, y):              # 두개 값 동시에 저장하기
    #     self.x = x
    #     self.y = y

    # 내가 원하는 기능의 메서드 ----------------------------
    # Point 인스턴스의 정보 출력하는 메서드(Method)
    def showPoint(self):
        print(f'현재 좌표값 ({self.x}, {self.y})')

    # Point 인스턴스에 해당하는 좌표를 그리는 메서드
    # x값 => 가로로 이동, y값 => 다음줄 \n
    def drowPoint(self):
        print('\n'*self.y, end='')
        print(' '*self._x + '★', end='')          # 두번 줄바꿈 하지 않도록 end='' 추가


# ---------------------------------------------------
# Point 인스턴스, 즉 객체 생성하기
p1=Point(10, 2)          # ()안에 아무것도 안 적어도 object는 무조건 상속된다 -> object는 모든 클래스의 디폴트
# p1._x=12345

# p1.setX(5)
# print( p1.getX() , p1.x )       # 일반적인 객체지향 언어는 직접적으로 수정하는걸 싫어해서 안되지만, 파이썬은 가능하다
#
# p1.x=1000
# print( p1.getX() , p1.x )

p1.drowPoint()

nums=[1,4,3,5,2,6,4,2,4,3]                                               # int 객체가 들어있는 것
points=[Point(5,5), Point(3,4), Point(4,2), Point(0,0)]               # type이 Point객체임, 포인트 객체가 들어있는 것
print('-'*10)
points[0].drowPoint()
print('='*10)
points[3].setX(10)
print( points[3].setX(10) )