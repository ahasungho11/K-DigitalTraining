#==================================================================
# Exception Handling : 예외처리
# 프로그램 실행 시 발생하는 오류(Wrror)에 대한 처리
# 오류가 발생해도 프로그램 중단하지 않고, 다음 코드를 실행할 수 있도록 처리
#==================================================================
try:
    num1, num2 = 10,0
    print(f'{num1}/{num2} = {num1/num2}')
    # print('END')
except Exception as Err:         # Exception은 어지간한 오류는 다 잡음
    print('에러발생', Err)
    # pass

finally:
    # 오류 발생 여부 상관없음 (반드시 실행해야 할 코드가 있다면 입력) => 파일 입출력할 때 써주는 경우(多)
    # 무조건 실행
    print('finally!!!')

print('END')                     # 예외가 안생길 것 같은 코드는 따로 빼주는게 좋지

# 단, 최상위 한단계 밑인 Exception을 먼저 써버리면 하위에 있는 예외들은 잡히지 않음
# - 하위 범위인 것들부터 차례로 작성할 것

try:
    file = open('flower.jpg', mode = 'r')
    print('file.read()')
    file.close()
except Exception as Err:
    print(f'ERROR 발생 : {Err}')

#=> 부르기 전에 확인하면 되지

import os
if os.path.exists('flower.jpg')
    file = open('flower.jpg', mode = 'r')
    print('file.read()')
    file.close()
else:
    print('없는 파일입니다.')

#24

# 오류 일부러 발생시키기
# ex) 비밀번호 횟수 제한 두고, 초과하면 오류 발생 시키는 것
