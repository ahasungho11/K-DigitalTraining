#==================================================================
# 프로그램 기능 구현상 강제로 예외 발생시키기
# raise 예외객체
#==================================================================
num = int(input('3의 배수 입력 : '))

if num %3 != 0:
    print(f'{num}은 3의 배수가 아닙니다.')
    raise Exception('3의 배수 오류')

# except Exception:
#     print('ERROR 발생')

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    # def fly(self):
    #     print('ㅁㄴㅇㄹ')
    pass

e = Eagle()
e.fly()

# 반드시 고쳐서 (오버라이딩) 쓰게끔 만들고 싶을 때, raise를 씀