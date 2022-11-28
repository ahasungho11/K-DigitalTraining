# mysql이든 oracle이든 DB프로그램에 맞춰서 연동해야 함
# host = 'localhost'나 '127.0.0.1' 둘중 하나로 일단 써도 됨

# 모듈 로딩
import pymysql
import pandas as pd

# 1) DB연결
conn = pymysql.connect(host='localhost', user='root', password='fkfk2rj2@!##H',
                       db = 'sakila', charset='utf8')

# 2) 커서 객체 생성
cur = conn.cursor()

# 3) 쿼리 실행
cur.execute('select * from language')
# 여기서 다양한 쿼리 문장이 들어가겠지?

# 4) fetchall() : 모든 검색 데이터 가져오기
rows = cur.fetchall()             # 모든(all) 데이터를 가져옴
print(rows)                       # for문 써서 rows를 하나씩 row를 인쇄할 수도 있겠지

language_df = pd.DataFrame(rows)  # DataFrame 형태로 바로 변환가능
print(language_df)

cur.close()     # 5) 커서 객체 닫기
conn.close()    # 6) DB 연결 닫기

# 쿼리가 바뀔 뿐, 전체적인 패턴은 같다고 보면 됨
# (cur.execute(~) 이부분)

# ---------------------------------------------------------------------------
# 조회를 할 때와 수정을 할 떄는 다름
# 1) 조회
import pymysql
conn = pymysql.connect()
#연결자 = conn
cur = conn.cursor()
sql = 'select * from language'
cur.execute(sql)
rows = cur.fetchone()

# ---------------------------------------------------------------------------
# 2. 추가 : INSERT, UPDATE, DELETE
# 5번째, '실행 결과 확정' 과정이 있어야 함 => 연결자.commit()
# commit() : 데이터를 추가, 수정, 삭제 등의 작업을 수행한 다음에 실행

#8 슬라이드 확인
import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='root', password='fkfk2rj2@!##H',
                        db = 'sakila', charset='utf8')
cur = conn.cursor()

query = """
select c.email
from customer as c
    inner join rental as r
    on c.customer_id = r.customer_id
where date(r.rental_date) = (%s)
"""

# query = """
# select c.email
# from customer as c
#     inner join rental as r
#     on c.customer_id = r.customer_id
# where date(r.rental_date) = '2005-06-14'
# """

cur.execute(query, ('2005-06-14'))   # %s에 순서대로 들어가겠찌
rows = cur.fetchall()                # 모든 데이터를 가져옴

for row in rows:
    print(row)

cur.close()
conn.close()

