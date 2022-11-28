# -------------------------------------------------------------------------------------
# sqlclass_db 사용
use sqlclass_db;

** 셀프조인

# drop table if exists customer;
# 같은 스크립트에서 작업할 때, 
# 다른 db의 이름이 같은 table을 생성하려고 하는데, drop하지 않으면 빨갛게 밑줄이 그어짐
# 흔히 테이블 만들기 전에 행하는 작업

create table customer
	(customer_id smallint unsigned,
	 first_name varchar(20),
	 last_name varchar(20),
	 birth_date date,
	 spouse_id smallint unsigned,
	 constraint primary key (customer_id));

# 생성된 customer 테이블 확인
desc customer;

# customer 테이블에 데이터 추가
insert into customer (customer_id, first_name, last_name, birth_date, spouse_id)
values
(1, 'John', 'Mayer', '1983-05-12', 2),
(2, 'Mary', 'Mayer', '1990-07-30', 1),
(3, 'Lisa', 'Ross', '1989-04-15', 5),
(4, 'Anna', 'Timothy', '1988-12-26', 6),
(5, 'Tim', 'Ross', '1957-08-15', 3),
(6, 'Steve', 'Donell', '1967-07-09', 4);

select * from customer;

insert into customer (customer_id, first_name, last_name, birth_date)
values (7, 'Donna', 'Trapp', '1978-06-23');

select * from customer;

select 
	cust.customer_id,
	cust.first_name,
	cust.last_name,
	cust.birth_date,
	cust.spouse_id,
	spouse.first_name as spouse_firstname,
	spouse.last_name as spouse_lastname
from customer as cust

	join customer as spouse
	on cust.spouse_id = spouse.customer_id;

# 도나씨는 spouse가 없으므로 출력되지 않음
# -------------------------------------------------------------------------------------
# CH7 ------------------------------------------------------------------------
use testdb;

create table string_tbl (
	char_fld char(30),
	vchar_fld varchar(30),
	text_fld text
	);

insert into string_tbl (char_fld, vchar_fld, text_fld)
values ('This is char data ',
		'This is varchar data ',
		'This is text data');
	
select * from string_tbl;

update string_tbl
set text_fld = 'This string didn''t work, but it does now';

update string_tbl
set text_fld = 'This string didn\'t work, but it does now';

select * from string_tbl;

insert into string_tbl (char_fld, vchar_fld, text_fld)
values ('This string is 28 characters',
'This string is 28 characters',
'This string is 28 characters');

select length(char_fld) as char_length,
length(vchar_fld) as varchar_length,
length(text_fld) as text_length
from string_tbl;

select * from string_tbl;

# ================================================================================
use sakila;

1) 문자열 데이터 처리
# char과 varchar의 연산속도 차이는 크게 없다고 할려진 상태
# escape문자 ('',\')
#  -> 작은 따옴표를 하나 더 추가
#  -> 백슬래시('\') 문자 추가

- quote() : 전체 문자열을 따옴표로 묶고, 문자열 내의 작은 따옴표에 escape 문자를 추가

- length() : 문자열의 개수 반환

- position() : 부분 문자열의 위치 반환(mysql은 인덱스 1부터 시작), 찾을 수 없을 경우 0을 반환

- locate('문자열', 열이름, 시작위치) : 특정 위치의 문자부터 검색, 검색의 시작 위치 정의

- strcmp('문자열1', '문자열2')
# ASCII, UNICODE 등 Table (자주 봐야겠지)
# 대소문자의 10진수 숫자로 연산을 한다고 보면 됨
# a-b > 0 =>  a>b,  -1반환 
# a-b = 0 =>  a=b,   0반환
# a-b < 0 =>  a<b,  1반환
# ex) 'cde' > 'abc'   : 이미 c가 a보다 더 크니까
# 숫자 < 대문자 < 소문자 (크기)

select strcmp('12345', '12345') 12345_12345,
strcmp('abcd', 'xyz') abcd_xyz,
strcmp('abcd', 'QRSTUV') abcd_QRSTUV,       # 다시 확인
strcmp('qrstuv', 'QRSTUV') qrstuv_QRSTUV,   # 0으로 반환되는 것은 다시 공지
strcmp('12345', 'xyz') 12345_xyz,
strcmp('xyz', 'qrstuv') xyz_qrstuv,
strcmp('bcd', 'cde') bcd_cde;

insert into string_tbl(vchar_fld)
values('abcd'),
	  ('xyz'),
	  ('QRSTUV'),
	  ('qrstuv'),
      ('12345');

- like 연산자, regexp 연산자
- -> like '%y'나 regexp'y$' 같음

# like 또는 regexp 연산자 사용
# 0 : false
# 1 : true

- concat() : 문자열 추가 함수, 각 데이터 조각을 합쳐서 하나의 문자열 생성
  -> concat() 함수 내부에서 date(create_date)를 문자열로 변환
  => select concat(first_name, ' ', last_name,
  ' has been a customer since ', date(create_date)) as cust_narrative

  - insert('문자열', 시작위치, 길이, '새로운 문자열') : 해당 위치부터 넣고, 기존값있으면 밀어내고
 -> select insert('goodbye world', 9, 0, 'cruel');         (0이기 때문에)
 -> select insert('goodbye world', 1, 7, 'hello');         (1부터7까지 덩어리를 덜어내고)

 - replace('문자열', '기존 문자열', '새로운 문자열') 
 - substr('문자열', 시작위치, 개수)

2) 숫자 데이터
- ceil(72.445)=73 : 가장 가까운 정수로 올림
- floor(72.445)=72 : 가장 가까운 정수로 내림
- round(72.0909,1)=72.1 : 반올림 (소수점 이하 n자리까지 나타내기)
- truncate(72.0956,1)=72.0 : 원치 않는 숫자를 버림 (소수점 이하 n자리까지 나타내기)
- sign() : 값이 음수면 -1, 0이면 0, 양수면 1을 반환
 
3) 시간 데이터 처리 (** 많이 쓰게 될)
(1) datetime 기본 형식 : YYYY-MM-DD HH:MI:SS
'2022-08-01 09:30:00'의 문자열로 구성
- 기존 date, datetime, time 열에서 데이터 복사
- date, datetime 또는 time을 반환하는 내장 함수 실행
 -> date(YYYY-MM-DD)
 -> datetime(YYYY-MM-DD HH:MI:SS)
 -> timestamp(YYYY-MM-DD HH:MI:SS)
 -> time(HHH:MI:SS)

(2) cast('지정한 값' as 변환타입) 함수 : 지정한 값을 다른 데이터 타입으로 변환

select cast('2022-08-01 14:27:27' as datetime);

select cast('2022-08-01' as date) date_field,
	   cast('14:27:27' as time) time_field;
	  
mysql은 날짜 구분 기호에 관대
'2019-09-17 15:30:00'
'2019/09/17 15:30:00'
'2019,09,17,15,30,00'
'20190917153000'
=> 모두 똑같은 결과로 나옴

select cast('2019-09-17 15:30:00' as datetime);
select cast('2019/09/17 15:30:00' as datetime);
select cast('2019,09,17,15,30,00' as datetime);
select cast('20190917153000' as datetime);


cast() : 지정한 값을 다른 데이터 타입으로 변환
 i) datetime값을 반환하는 쿼리 생성
 
 select cast('2022-08-01 22:24:24' as datetime);

  ii) date 값과 time 값을 생성
  
 select cast('2022-08-01' as date) as date_field,
 cast('108:17:57' as time) as time_field;

(3) str_to_date()
: 형식 문자열의 내용에 따라 datetime, date 또는 time값을 반환

select str_to_date('Sept 17, 2019', '%M %d, %Y') as return_date;
# 똑같은 형태로 해주기 위해 콤마(,) 위치를 맞춰주는 것임 => 값들이 똑같이 대치될 수 있도록

(4) 현재 날짜 시간 생성
=> current_date(), current_time(), current_timestamp()

select current_date(), current_time(), current_timestamp();

(5) date_add()
: 지정한 날짜에 일정 기간(일, 월, 년 등)을 더해서 다른 날짜를 생성

select date_add('2022-08-01', interval 5 day);

select date_add(current_date(), interval 5 month);

update rental
set return_date = date_add(return_date, interval '3:27:11' HOUR_SECOND)
where rental_id = 99999;                         (시간 자료)  (기간 자료형)
# 테이블의 변화를 주지않기 위해서 99999를 적은 것

(6) last_day(date)
: 해당 월의 마지막 날짜 반환

select last_day('2022-08-01')

(7) dayname(date)
: 해당 날짜의 영어 요일 이름을 반환

select dayname('2022-08-01');

(8) extract()
: date의 구성 요소 중 일부 추출, 기간 자료형으로 원하는 날짜 요소를 정의

select extract(year from '2019-09-18 22:19:05');

(9) datediff(date1, date2)
: 두 날짜 사이의 기간(년, 주, 일)을 계산
  (시간 정보는 무시)
  
select datediff('2019-09-03', '2019-06-21');

4) 변환 함수
(1) cast() : 데이터를 한 유형에서 다른 유형으로 변환할 때 사용
 - cast(데이터 as 타입)
 
 select cast('1456328' as signed integer);
 # 문자열 -> 숫자
 select cast('20220101' as date);
 select cast(20220101 as char);
 select cast(now() as signed); 
 