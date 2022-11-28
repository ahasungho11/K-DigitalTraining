from selenium import webdriver

driver = webdriver.Chrome('C:\workspace\chromedriver')
driver.get('https://www.google.com')

print(driver.current_url)
# driver.quit()

#---------------------------------------------------------------

# - selenium이 실행되면 크롬이 바로 열리고
# - 끝낼 때는 driver.quit() 를 하면 됨
#
# - 왼쪽 하단에 javascript로 지점번호가 나옴
#  => 이게 바뀌면서 가져오는

#---------------------------------------------------------------

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:\workspace\chromedriver')
driver.get('https://www.coffeebeankorea.com/store/store.asp')

driver.execute_script('storePop2(1)')
# execute_script('자바스크립트명') => 자바 스크립트 실행 시키는 것
# 핵심은 자바스크립트를 파악해야 함
# -무엇인가를 누르면 자바 스크립트를 실행한다는 것을 파악하고 난 후

# 현재의 html 소스를 저장
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')



# print(soup)

store_names = soup.select('div.store_txt > p.name > span')  # 매장 이름
store_name_list = []
for name in store_names:
    store_name_list.append(name.text)  # name.text = name.get_text()

print('매장 개수: ', len(store_name_list))
print(store_name_list)

store_address = soup.select('p.address > span')  # 매장 주소
store_address_list = []

for addr in store_address:
    print(addr.get_text())  # addr.text = addr.get_text()

#---------------------------------------------------------------

# 자바 스크립트를 실행했을 때 나오는 html을 갖고 오는 것이고
# popup창은 또 다름.
# 시간이 부족해서 덜 받고 지나갈 수도 있으니 time.sleep(2) 으로 지연을 주는 것

#---------------------------------------------------------------










