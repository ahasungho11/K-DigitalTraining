from urllib.request import urlopen
from bs4 import BeautifulSoup

def parse_use_find(html):

    page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Ytnqy3ZBxPY')
    html = BeautifulSoup(page.read(), 'html.parser')

    ''' 보통 주석을 내부에 단다고 함
    기후 정보 분석: find() 함수 사용
    :param html : 웹사이트 전체 html
    :return:
    '''
    # print('parse_use_find()')
    # 디버깅 키 : F8(한 라인씩 실행=>Step over), F7(함수 내부로 이동=>Step into)
    seven_day = html.find('div', id='seven-day-forecast')
    print(seven_day)
#~5) 전체 사이트를 받아오고 seven_day로 줄임

#6~) 데이터를 줄이는 중
    forecast_items = seven_day.find_all('div', class_='tombstone-container')
    print(len(forecast_items))

# 7) 다시금 break point 걸어 놓고 디버깅 시작
# 클릭하면 복사할 수 있으니, 따로 열어서 확인해보도록. 줄어든 것을 확인
# 에디터로 확인하는 것도 좋음, 간단하게 보기 편하게 살짝 편집 해도 되고
# 필요하면 반복되는 패턴 중 하나를 떼어다가 연습해도 되겠고
# 디버그 탭에서 추가하면서 바로 확인도 가능

    for day in forecast_items:
        if (day.find(class_='temp') is not None):  # class='temp'가 있는 경우에만 찾음
            period = day.find('p', class_='period-name').text
            print(period)
            # 중간 중간에 프린트를 넣는 것도 개발자의 역량 -> 나중에 빼면되니까

            short_desc = day.find('p', class_='short-desc').text
            print(short_desc)
            # 계속해서 디버깅 하면서 진행 중

            temp = day.find('p', class_='temp').text
            # 해당 브레이크 포인트 직전까지만 실행되니, 포인트를 확인하고 싶으면 f8로 실행하면서 디버깅 탭 화면 봐주기

            img_desc = day.find('img')['title']
            #태그('img'), 속성명('title')

            print('-'*80)
            print('[Period]: {0}'.format(period))
            print('[Short desc]: {0}'.format(short_desc))
            print('[Temperature]: {0}'.format(temp))
            print('[Image desc]: {0}'.format(img_desc))
        print('-'*80)


def parse_use_select(html):
    print('parse_use_select()')



page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Ytnqy3ZBxPY')
html = BeautifulSoup(page.read(), 'html.parser')
# 객체 생성
# print(html) # 중간에 당연히 확인하면서

# 1) 전체적인 틀만 만들어 놓은 것 (함수 정상 호출 되는 지 확인)
# 2) 1차적으로 들어가는 첫부분 찾아서 호출 (seven_day)
# 3) break point -> 이전부터 진행하다가 멈추는 지점 (숫자 옆에 클릭)
# 4) shift + f9로 디버깅 시작
# 5) 아래쪽 디버그 탭 확인 -> 어떻게 돌아가고 있는지 확인 가능 -> ctrl+f2로 확인 후 정지
# 6) 줄여 놓은 데이터를




