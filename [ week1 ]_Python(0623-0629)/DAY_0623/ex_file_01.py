#-------------------------------------------------------------------------------------
# 파일 읽고 쓰기 => 파일 입출력(I/O)  (Input/Output)
#-------------------------------------------------------------------------------------

import fileinput

filename='mydata.txt'

# 파일 쓰기
# (1) 파일 열기
# mode 'w' : 파일 없으면 -> 생성 후, 쓰기  /  파일 있으면 -> 지우고, 쓰기 (덮어씀)
# mode 'a' : 파일 없으면 -> 생성 후, 쓰기  /  파일 있으면 -> 덧붙이기             (append)

file = open(filename, mode='a', encoding='utf-8')

# open 함수가 input과 output을 통해 stream을 만듦
# stream => file을 읽고 쓸 수 있는 통로

# (2) 파일에 데이터 쓰기
file.write('Good\n')
file.write('Happy\n')
file.write('1234\n')
# 정수 더라도 무조건 따옴표를 넣어서 문자로 입력해 주어야 함!

# (3) 파일 닫기
file.close()

#-------------------------------------------------------------------------------------

# 파일 읽기
# (1) 파일 열기
# mode = 'r'  ==> read의 약자 (기본값)
file = open(filename, mode = 'r')

# (2) 파일 읽기
data = file.read()                      # read는 전체를 다 읽음
print(f'read data => {data}')
print(f'read data type => {type(data)}')

file.seek(0)
# 커서를 0번자리, 즉 젤 앞으로 옮긴다.
data2 = file.read()                      # read는 전체를 다 읽음
print(f'read data2 => {data2}, len => {len(data2)}')
# read를 해버리면 전체를 읽음 & 커서(file point)가 처음부터 읽은 부분을 다 지나가면서 커서를 옮겨감 -> 끝에 커서 이동 -> 이동할 거리 0

file.seek(0)
# file point 제일 앞으로
#-----------------------------
# 파일에서 1줄 읽기                                -------> 반복문 활요해서 죽 읽어주기
data3 = file.readline()
print(f'read data3 => {data3}, len => {len(data3)}')

data3 = file.readline()
print(f'read data3 => {data3}, len => {len(data3)}')

#줄바꿈 문자까지 한줄 => 두번하니까 두번째 줄을 읽게 되는 것이지
#-----------------------------
# 1줄씩 읽어서 리스트에 담아서 가져오기
# .readlines()를 하면, 줄단위로 끊어서 리스트에 담아줌
data4 = file.readlines()
print(f'read data4 => {data4}')
#-----------------------------
#
data5 = file.read(2)                      # read는 전체를 다 읽음
print(f'read data5 => {data5}')
#-----------------------------
# (3) 파일 닫기
file.close()





#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
