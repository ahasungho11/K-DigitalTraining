# 모듈 로딩
import pymysql

# 함수, 입력 데이터 정리
def mysql(ddd, sss):
    conn = pymysql.connect(host='localhost', user='root', password='fkfk2rj2@!##H',
                           db='teamproject', charset='utf8')
    curs = conn.cursor()

    curs.executemany(ddd, sss)
    conn.commit()
    conn.close()

data1 = (
('KHD', '강호동', 1970, '경북', '011', '22222222', 182, '2007-07-07'),
('KJD', '김제동', 1974, '경남', 'null', 'null', 173, '2013-03-03'),
('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-09-09'),
('KYM', '김용만', 1972, '경기', '010', '44444444', 177, '2015-05-05'),
('KYM', '김용만', 1972, '경기', '010', '44444444', 177, '2015-05-05'),
('KYM', '김용만', 1972, '경기', '010', '44444444', 177, '2015-05-05'),
('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-04-04'),
('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12'),
('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-04-04'),
('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2008-10-10'),
('SDY', '신동엽', 1971, '경기', 'null', 'null', 176, '2008-10-10'),
('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-08-08')
)

sql1 = """
insert into user_table
(userID, userName, birthYear, addr, mobile1, mobile2, height, mDate)
values (%s, %s, %s, %s, %s, %s, %s, %s)
"""

data2 = (
(1, 'KHD', '운동화', 'null', 30, 2),
(2, 'KHD', '노트북', '전자', 1000, 1),
(3, 'KYM', '모니터', '전자', 200, 1),
(4, 'PSH', '모니터', '전자', 200, 5),
(5, 'KHD', '청바지', '의류', 50, 3),
(6, 'PSH', '메모리', '전자', 80, 10),
(7, 'KJD', '책', '서적', 15, 5),
(8, 'LHJ', '책', '서적', 15, 2),
(9, 'LHJ', '청바지', '의류', 50, 1),
(10, 'PSH', '운동화', 'null', 30, 2),
(11, 'LHJ', '책', '서적', 15, 1),
(12, 'PSH', '운동화', 'null', 30, 2)
)

sql2 = """
insert into buy_table
(num, userID, prodName, groupName, price, amount)
values (%s, %s, %s, %s, %s, %s)
"""

def mysql2(qqq):
    conn = pymysql.connect(host='localhost', user='root', password='fkfk2rj2@!##H',
                            db='teamproject', charset='utf8')
    curs = conn.cursor()

    curs.execute(qqq)
    rows = curs.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()


query1 = """
select u.userName, b.prodName, u.addr, concat(u.mobile1,u.mobile2) as '연락처'
from user_table as u
inner join buy_table as b
on u.userID = b.userID
"""

query2 = """
select u.userID, u.userName, b.prodName, u.addr, concat(u.mobile1,u.mobile2)
from user_table as u inner join buy_table as b
on u.userID = b.userID
where u.userID = 'KYM'
"""

query3 = """
select u.userID, u.userName, b.prodName, u.addr, concat(u.mobile1,u.mobile2) as '연락'
from user_table as u inner join buy_table as b
on u.userID = b.userID
order by u.userID
"""

query4 = """
select distinct u.userID, u.userName, u.addr
from user_table as u inner join buy_table as b
on u.userID = b.userID
where prodName is not null
order by u.userID
"""

query5 = """
select u.userID, u.userName, b.prodName, u.addr, concat(u.mobile1,u.mobile2) as '연락'
from user_table as u inner join buy_table as b
on u.userID = b.userID
where u.addr = '경북' or u.addr = '경남'
order by u.userID
"""

# 문제 해답 ------------------------------------------------------------------------------------------------------------
# 문제1.
mysql(data1,sql1)
mysql(data2,sql2)

# 문제2. 1)~5)
mysql2(query1)
mysql2(query2)
mysql2(query3)
mysql2(query4)
mysql2(query5)


query1 = """
select * from reg_7_year;
"""