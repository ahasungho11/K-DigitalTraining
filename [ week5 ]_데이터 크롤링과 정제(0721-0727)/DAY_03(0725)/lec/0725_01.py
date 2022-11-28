
# tbody(table body) 안에 매장 정보 다 있었움

# 페이지가 넘어가면서 번호가 넘어가면서 페이지 열림
# -> url 정보의 번호를 바꿔가면서 데이터를 찾도록
#
# - 페이지 넘버만 숫자로 바꿈 -> {0}~.format(~)
#
# - 굳이 변수 안주고 바로 tr뽑은 것에서 for문 돌리셨네
#
# - .string, .text 메서드
#
# -branches라는 리스트에 모든 정보 다 넣었기 때문에 이 변수로 곧바로 DF로 만듦
#
# 2번 문제
# - contains 쓰셨음 => 잘못 입력할 수 있으니 포괄적으로 검사
# - 받은 것을 곧바로 DF를 만듦
# - DF에서 values값만 뽑아서 tolist 함
#
# * 스크롤링 -> csv 만들기 -> 여기서 뽑아서
# * database에 담아서 하는 거는 다음주부터


import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class':'post-body'}).text
    return Content(url, title, body)

url = 'https://www.brookings.edu/blog/future-development/2018/01/26/deliveringinclusive-urban-access-3-uncomfortable-truths/'

content = scrapeBrookings(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)