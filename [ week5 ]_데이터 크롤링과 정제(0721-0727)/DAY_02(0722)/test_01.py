from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# 일단, 페이지에서 원하는 정보 뽑아내서 다 담아보자
resultDir = {'region': [], 'name': [], 'add': [], 'phone': [], 'state': []}
pick = [(0, 'region'), (1, 'name'), (3, 'add'), (5, 'phone'), (2, 'state')]  # td까지 타고 내려갔을 때, 지역[0], 이름[1], 주소[3], 전화번호[5]
count = 0

for num in range(1, 2):
    html = urlopen('https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=' + str(num) + '&sido=&gugun=&store=')
    bs = BeautifulSoup(html, 'html.parser')
    tbody = bs.find('tbody')
    rows = tbody.find_all('tr')

    for i in range(len(rows)):
        count += 1
        for n in pick:
            textR = rows[i].find_all('td')[n[0]].text
            resultDir[n[1]].append(textR)

# print(rows[0].find_all('td')[(0, 'region')[0]])
# print(resultDir[n[1]])

# 1번 실행 결과 - 화면 출력
for i in range(count):
    print('[  {0}]: 매장이름: {1}, 지역: {2}, 주소: {3}, 전화번호: {4}, 상태: {5}'.format(i+1, resultDir['name'][i], resultDir['region'][i], resultDir['add'][i], resultDir['phone'][i], resultDir['state'][i]))
print('전체 매장 수: {}'.format(count))
