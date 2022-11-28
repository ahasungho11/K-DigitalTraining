#----------------------------------------------------------
# File & Dir 관련 모듈
#----------------------------------------------------------
import os.path as path
import os

# os는 파일 저장과 같은 많은 운영 체제 관련 기능에 사용할 수있는 Python 내장 모듈

# 특정 폴더 존재 여부 체크 -> 폴더 없으면 생성하기
DIR_PATH='./Image/jpg/01'
print(path.exists(DIR_PATH))   # exists() 파일, 폴더 모두 확인 가능

# 폴더 만들 때 -> make directory

# os.mkdir(path, mode=0o777, *, dir_fd=None)   ->  폴더 1개만 만듦, 하위로 하나만 만드는 거라면 이거쓰기
# os.makedirs(name, mode=0o777, exist_ok=False) -> 상위~하위 폴더까지. 여러 개의 폴더를 만듦 (최종 마지막 기준으로 볼 것)

if not path.exists(DIR_PATH):
    # os.mkdir(DIR_PATH)
    # os도 마저 import 해야징
    os.makedirs(DIR_PATH)

# 특정 파일 존재 여부 체크
DATA_FILE=DIR_PATH+'/flower.jpg'
if not path.exists(DATA_FILE):
    print('파일 없음')

# 측정 경로 안에 존재하는 내용 리스트 화
datalist = os.listdir('./AddressBook')
print(datalist)

# os.listdir(path='.')
# 리스트로 경로
# os.scandir(path='.')
# 찾을 때
# -> 탐색 기능 활용

# + 서칭 추가
# os.listdir() : 디렉토리 내의 모든 파일과 디렉토리 목록을 list로 리턴합니다.
# os.scandir() : 디렉토리 내의 모든 객체(파일 속성 포함)에 대한 iterator를 리턴합니다.
# pathlib.Path.iterdir() : 디렉토리 내의 모든 객체(파일 속성 포함)에 대한 iterator를 리턴합니다.



# 시간관련 모듈
import time as t
print(t.time())
print(t.localtime(t.time()))

curTime=t.localtime(t.time())
print(curTime.tm_year, curTime.tm_wday, curTime.tm_hour)

# 2022-06-24 or 2022/06/24 or 24/06/2022 => 사용자 임의로 표현하는 (format()처럼) // 문자처럼 만드는 것

for num in range(10):
    t.sleep(1.0)
    # print(num)
    print('[메롱]', end='')

