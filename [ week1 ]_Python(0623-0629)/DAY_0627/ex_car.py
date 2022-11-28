#==================================================================
# 클래스 형식 (frame)
# class 클래스명:
#       클래스 변수
# def __init__(~ ):  인스턴스 변수
# def ~           : 하고싶은 기능들
#==================================================================



# 현대 자동차를 표현하는 데이터 타입. 즉, class 생성
# 클래스명 :
# 속성/특징 : 제조사 //  차번호, 차종류, 색상
#           -> '현대자동차'라고 했으니, 클래스 변수로 정해줘야겠지?
#           -> 즉, 클래스/인스턴스 변수로 쓸 것을 정하기
# 역할/기능 : 이동한다, 정지한다, 차정보 출력한다
#           -> 이동한다 => 000 자동차가 xx에서 yy로 간다.
#           => 000은 변수로 들어가 있음, xx와 yy는 파라미터로 받아야지
#           -> 정지한다 => 000 자동차가 xxx에 정지한다.
# 매번 정지하는 곳이 다르니, 매번 xxx를 파라미터로 받아야지
#           -> 차정보 출력한다 => 제조사, 차종류, 차번호, 색상
#           => 이미 인스턴스 변수로 갖고 있으니 파라미터를 받을 필요가 없겠지

# 입력한 변수가 없으면, 파라미터로 받아야지

#==================================================================

class car:
    brand = '현대자동차'

    def __init__(self, carNum, carGubun, carCol):
        self.carNum = carNum
        self.carGubun = carGubun
        self.carCol = carCol

    def move(self, start, des):
        print(f'{self.carGubun}은 {start}에서 {des}로 간다.')

    def stop(self, spot):
        print(f'{self.carGubun}은 {spot}에 정지한다.')

    def info(self, brand):
        # print(f'{self.carGubun}의{brand})
        print(f'차번호 : {self.carNum}')
        print(f'차색상 : {self.carCol}')
        print(f'제조사 : {car.brand}')

# 확인할 때, 객체를 우선 만들어야지 => a처럼
# self는 입력하지 않아도 되지 당연
a = car(123,'sss', 'G')
a.move('범어네거리','동성로')

# 자동차 데이터 저장 => 자동차 인스턴스 생성 => 클래스명() --->  __init__
myCar1 = car(1234,'suv', 'pink')   # 객체 생성한 것
myCar1.move('칠곡iC','경산IC')

# 정수 10개  <===>  데이터 10개 저장
# 1)
nums=[]
for n in range(10): nums.append(n*10)

# 2)
cars=[]
for n in range(10): cars.append(car(n*1111, 'suv', 'pink'))
for car in cars:
    nums, type, color = input('차번호, 차종류, 차색상 : ').slplit(',')
    print(f'{car.carNum}')
for car in cars:
    print(f'{car.carGubun}')

# 인스턴스 변수, 클래스 변수, 

# 기존의 클래스에 있는 것 다 가져오고, 필요한 기능만 추가하고자 할 때
# => 상속
#98

