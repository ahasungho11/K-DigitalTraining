# db 만들기
create database shoppingmall;

# db 사용하기
use shoppingmall;

# table 만들기1
CREATE TABLE user_table
		   (userID CHAR(8) not null primary key, # 사용자 ID
			userName VARCHAR(10) not null, # 이름
			birthYear int not null, # 출생년도
			addr CHAR(2) not null, # 지역(경기,서울, 경남, 2글자)
			mobile1 CHAR(3), # 휴대폰 국번
			mobile2 CHAR(8), # 휴대폰 나머지 전화번호 (하이픈 제외)
			height smallint, # 키
			mDate DATE); # 회원 가입일

# table 확인1
desc user_table;
select * from user_table;

# 테이블에 데이터 입력1
insert into user_table
(userID, userName, birthYear, addr, mobile1, mobile2, height, mDate)
values
('KHD', '강호동', 1970, '경북', '011', '22222222', 182, '2007-07-07'),
('KJD', '김제동', 1974, '경남', null, null, 173, '2013-03-03'),
('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-09-09'),
('KYM', '김용만', 1972, '경기', '010', '44444444', 177, '2015-05-05'),
('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-04-04'),
('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12'),
('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-04-04'),
('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2008-10-10'),
('SDY', '신동엽', 1971, '경기', null, null, 176, '2008-10-10'),
('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-08-08');

# 입력후, 테이블 확인
select * from user_table;

# table 만들기2
CREATE TABLE buy_table
			(num INT auto_increment not null primary key, # 순번
			userID CHAR(8) not null, # 아이디 (FK)
			prodName CHAR(6) not null, # 물품명
			groupName CHAR(4) not null, # 분류
			price INT not null, # 단가
			amount SMALLINT not null); # 수량
			
# table 확인2
desc buy_table;
select * from buy_table;

# 테이블에 데이터 입력2
insert into buy_table
(num, userID, prodName, groupName, price, amount)
values
(null, 'KHD', '운동화', 'null', 30, 2),
(null, 'KHD', '노트북', '전자', 1000, 1),
(null, 'KYM', '모니터', '전자', 200, 1),
(null, 'PSH', '모니터', '전자', 200, 5),
(null, 'KHD', '청바지', '의류', 50, 3),
(null, 'PSH', '메모리', '전자', 80, 10),
(null, 'KJD', '책', '서적', 15, 5),
(null, 'LHJ', '책', '서적', 15, 2),
(null, 'LHJ', '청바지', '의류', 50, 1),
(null, 'PSH', '운동화', 'null', 30, 2),
(null, 'LHJ', '책', '서적', 15, 1),
(null, 'PSH', '운동화', 'null', 30, 2);

# 입력후, 테이블 확인
select * from buy_table;

desc user_table;
desc buy_table;

2. 내부조인
1)

select u.userName, b.prodName, u.addr, concat(u.mobile1,u.mobile2) as '연락처'
from user_table as u inner join buy_table as b
on u.userID = b.userID

2)

select u.userID, u.userName, b.prodName, u.addr, concat(u.mobile1,u.mobile2)
from user_table as u inner join buy_table as b
on u.userID = b.userID
where u.userID = 'KYM'

3)

select u.userID, u.userName, b.prodName, u.addr, concat(u.mobile1,u.mobile2) as '연락'
from user_table as u inner join buy_table as b
on u.userID = b.userID
order by u.userID

desc user_table;
desc buy_table;

4)

select distinct u.userID, u.userName, u.addr
from user_table as u inner join buy_table as b
on u.userID = b.userID
where prodName is not null
order by u.userID

5) 

select u.userID, u.userName, b.prodName, u.addr, concat(u.mobile1,u.mobile2) as '연락'
from user_table as u inner join buy_table as b
on u.userID = b.userID
where u.addr = '경북' or u.addr = '경남'
order by u.userID