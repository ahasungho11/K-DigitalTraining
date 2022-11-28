# 주소표시줄 - 경로
# ex) C:\Users\ahasu\Desktop\Python\first\Data\home.html
# -> 해당 컴퓨터에 있을 때는 되지만, 아니라면 불가
#-------------------------------------------------------------------------------------
# PATH -> 경로
# - 절대경로 : 파일 및 폴더 존재하는 위치의 경로 예) C:\Users\ahasu\Desktop\관리하자
# - 상대경로 : 현재 코드 파일 기준으로 경로를 지정 (본인이 기준)
#   .  : 현재위치
#   .. : 상위 한단계 위

# 내 프로젝트 안의 것이라면 상대경로 써도 무방
# 다픈 곳에 있는 파일을 쓰고 싶은 경우라면 절대경로

#-------------------------------------------------------------------------------------
file = r'C:\Users\ahasu\Desktop\Python\first\Data\home.html'    # r로 하는 것을 권장
file= '../Data/home.html'
file = './html/home.html'
# 가고자 하는 경로의 파일들의 이름이 뜬다면 제대로 가는 것이 맞음
#-------------------------------------------------------------------------------------
# home.html 파일을 라인 단위로 읽어서 화면에 출력하기

file = open('./html/home.html', mode = 'r')
data = file.readline()
print(data)

# 파일 열기
file=open(file, mode = 'r')

data = file.read()
print(f'all data => {data}')

# 파일 닫기
file.close()


#-------------------------------------------------------------------------------------

# file = open(r'C:\Users\ahasu\Desktop\Python\first\Data\home.html', mode = 'r', encoding='UTF-8')
# data = file.readline()
# print(data)
# file.close()


# file = open('./html/home.html', mode = 'r')
# data = file.readline()
# print(data)
#-------------------------------------------------------------------------------------
# 경로 제대로 적기 -> r을 넣든지 \\로 고치든지
#

# 파일 열기
file = open(r'C:\Users\ahasu\Desktop\Python\first\Data\home.html', mode = 'r', encoding='utf-8')

# 파일 읽기
data = file.read()
print(f'all data => {data}')

while True:
    data = file.readline()
    if not data: break
    data = data.strip()
    if len(data) > 0: print(data)

# 파일 닫기
file.close()


# with 파일 as 구문  -  close를 잊을 수도 있으니 사용 권장
# file이란 변수에는 str이 들어가야, 객체는 안됨
# with open(file, mode = 'r', encoding='utf-8') as file:
#     while True:
#         data = file.readline()
#         if not data: break
#         data = data.strip()
#         if len(data) > 0: print(data)


# UnicodeDecodeError: 'cp949' codec can't decode bytes in position : illegal multibyte sequence
 # -> [ encoding='utf-8 ] 추가하기