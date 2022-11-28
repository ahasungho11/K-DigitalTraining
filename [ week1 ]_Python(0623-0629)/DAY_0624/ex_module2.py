#------------------------------------------------------------------------
# 모듈(module) : 하나의 파이썬(.py) 파일
#               특정 목적에 관련된 변수, 함수, 클래스 존재
#               필요한 파일에서 사용 가능 함
# 사용법 => import 모듈명
#------------------------------------------------------------------------
# # 모듈 포함 하기 (as 써서 별칭) -> 모듈 안 기능 사용하기
# import math as m
# print(m.factorial(5), m.pi)
#
# # 특정 모듈 안에서 특저 함수 가져오기 -> 모듈 안 기능 사용하기
# from math import factorial, pi, fabs
# print(factorial(5), pi, fabs(-30))
#
# # math함수의 모든 것을 가져오기
# from math import *
#
# # 모듈에 있는 것을 갖고 온 함수보다 사용자 정의 함수가 우선적으로 쓰임

#
import ex_func_3
print(ex_func_3.year, ex_func_3.printYear())


