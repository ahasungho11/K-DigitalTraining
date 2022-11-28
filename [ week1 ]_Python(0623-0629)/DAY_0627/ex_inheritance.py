#==================================================================
# 상속(Inheritance) : 기존 클래스의 모든 것을 가져다가 사용하는 것 => 재사용 or 확장
# 표현 : class 클래스명(클래스명) :
#==================================================================
class A:
     def __init__(self, x, y):
         self.x = x
         self.y = y

     def displayInfo(self):
        print(f'A => self.x, self.y')

class B(A):             # A(부모), B(자녀)
    def calc(self):
        print(self.x * self.y)

class C(B):
    def add(self):
        print(self.x * self.y)

    def calc(self):
        print(self.x * self.y, self.x + self.y)

# 상속받고 수정을 하면 수정한 것(오버라이딩)이 우선시
# - 상속받은 함수를 수정하는 것

# 오버로딩 => 재료가 다름 (상속과 무관)
# - 파이썬에서는 기능 지원x

# b=B() # 오류나지
b=B(5,3)
b.calc()
c=C(5,2)
c.calc()