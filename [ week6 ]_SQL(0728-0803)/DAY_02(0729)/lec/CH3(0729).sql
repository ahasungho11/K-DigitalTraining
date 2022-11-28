# 0729
# 조인 => 테이블 연결
# order BY 여러 열이 들어갈 수 있으며, 왼쪽으로 부터 우선순위로 하여 정렬 적용

show databases;
use sakila;

# * (asterisk): 모든 열을 지정
# 최종 결과셋에 포함할 항목(열)을 결정
select * from language;

# 일부 열만 검색 (특정 컬럼 내용만 보고자 할 때)
select name, last_update from language;


# 없는 컬럼을 임의로 생성할 수도 있음
# 가상 컬럼들을 select를 해서 생성할 수 있음 (숫자or문자열, 표현식, 내장 함수 호출 및 사용자 정의 함수 호출)
# -> language usage, lang_pi_value 두개는 컬럼은 원래 없었는데, select 하면서 생성된 것
# -> DF에서 없는 컬럼명을 입력하면 자동으로 끝에 생성되는 것과 비슷 (or insert로 원하는 곳에 삽입하는)
# -> 각각은 입력한 대로 데이터가 들어간 것이고

select language_id,
	'COMMON' language_usage,
	language_id * 3.14 lnag_pi_value,
	upper(name) language_name         # upper(name) 내장함수. 대문자로 변경
from language;


select language_id,
	'COMMON' AS language_usage,
	language_id * 3.14 AS lang_pi_value,
	upper(name) AS language_name
from language;

# 17
# as 키워드를 생략할 수도, 입력할 수도 있음 (for 가독성 향상)

# 중복 제거 (like set()함수)
# -> distinct 키워드 사용 : 중복 제거 
# -> 남용 자제 할 것. 내부적으로 정렬이 먼저 이루어지는 작업이므로 시간이 소요되기 때문에

select all actor_id from film_actor order by actor_id;
# all은 디폴트값임. 사실상 select 뒤에 아무 단어도 없으면 all이 들어간 셈

select distinct actor_id from film_actor order by actor_id;

# from절 -----------------------------------------------------------------
# 영구 테이블(permanent table) : 기존 테이블, create table문으로 생성
# 파생 테이블(derived table) : 하위 쿼리에서 반환하고 메모리에 보관된 행들
# 임시 테이블(temporary table) : 잠시 사용하기 위해. DB 세션이 닫힐 때 사라짐
# 가상 테이블(virtual table) : 뷰(view), create view문으로 생성
# -> sakila > views 항목에 보면 실제 테이블을 저장하는 것은 아니고, script를 저장해 두었다가 실행할 때 보여주는 것임
# -> view를 보여줌

# 서브쿼리(subquery) -> 파생 테이블
# from 서브쿼리 => 서브쿼리의 결과에서 select 출력 선택

# 서브쿼리 내용
select first_name, last_name, email from customer
where first_name = 'JESSIE';
# 아래의 subquery가 복잡할 경우, 이렇게 떼어서 생각해보는 것이 도움이 됨

select concat (cust.last_name, ', ', cust.first_name) as full_name   # as 생략할 수도 있음
# select cust.last_name, cust.first_name 그냥 이렇게 써도 되지

from
    (select first_name, last_name, email
     from customer
     where first_name = 'JESSIE')
	 as cust;  

# 해당 서브쿼리를 별칭 cust로 정한 것 -> concat을 사용하여 full_name이라는 이름으로 정한 컬럼으로 뽑아준 것
# concat(문자열1, 문아졀2, ...) : 둘 이상의 문자열을 순서대로 합쳐서 반환

create temporary table actors_j
(actor_id smallint(5),
first_name varchar(45),
last_name varchar(45)
);

# 즉, 서브쿼리의 결과가 테이블이 된다는 것	
# 임시 테이블 - temporary를 붙이는지 여부만 다르고, 테이블 만드는 것과 똑같음
# 5자리 공간을 확보하고 채워 넣어라 (출력시, 자리수를 말한느 것임  ex) print('{:5d}') => 이런 것과 비슷
# 지금 당장은 임시 테이블 예시지만, 실제로는 어디에든 쓰기 위해 만드는 경우가 많다고 보면 됨


# 원본 쿼리 #1 : J로 시작하는 last_name을 검색
select actor_id, first_name, last_name
from actor where last_name like 'J%';

# 헷갈린다면 위와 같이 떼어서 생각해보고 실행해도 됨

# 원본 쿼리 #1의 출력 결과를 actors_j 테이블에 데이터 추가
insert into actors_j
select actor_id, first_name, last_name
from actor where last_name like 'J%';

select * from actors_j;

# 가상 테이블(View) ----------------------------------------------------
# 우선적으로 view를 통해 먼저 알아보고, 작업을 수행할 수도 있음
# 복잡한 쿼리문을 매번 사용하지 않고, 가상 테이블로 만들어서 쉽게 접근함
# -> 모듈을 만들어 놓는 것과 비슷하다고 보면 될 듯

# 가상 테이블 (view) 생성
create view cust_vw as
select customer_id, first_name, last_name, active
from customer;

# 가상 테이블의 활용
select first_name, last_name from cust_vw   # 뷰(가상 테이블)에서 가져와서 활용
where active=0;

# 복잡한 원본 테이블에서, 임시로 필요한 것을 뽑아서 -> 하나의 가상테이블을 만들어서 편하게 쓰겠다는 것

# view 삭제
drop view cust_vw;

# [ Where절 ] -------------------------------------------------------------
# JOIN(INNER JOIN, 내부 조인)
# on 뒤에 입력하는 두 테이블 사이의 공통된 부분이 있어야 조인이 가능함
# -> 행의 갯수도 같아야 한다는 것!!

select customer.first_name, customer.last_name,
	   time(rental.rental_date) as rental_time
from customer inner join rental
	   on customer.customer_id = rental.customer_id
where date(rental.rental_date) = '2005-06-14';

# date() 함수 : YYYY-MM-DD 정보 리턴
select date('2022-07-29 09:02:03');         # 별칭을 입력하지 않으면 select 뒤에 것이 컬럼명으로
select date('2022-07-29 09:02:03') as day1; # 별칭을 입력하면 그것이 컬렴명이 됨

# time() 함수 : HH:MI;SS 정보 리턴
select time('2022-07-29 09:02:03');

# as 키워드를 써서 좀 더 간단하게
# -> from 에서 불러오는 절이니까, 불러오면서 별칭을 주고, select에서 쓰는 것을
# -> 각 테이블의 별칭을 할당하고, 쿼리 전체에서 해당 별칭을 사용 (AS 키워드 사용)

select c.first_name, c.last_name,
		time(r.rental_date) rental_date
from customer c inner join rental r
		on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14';

# 위의 것을 as 키워드를 넣어 쓴다면
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from customer as c inner join rental as r
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14';

# where 조건절
select title, rating, rental_duration
from film
where rating='G' and rental_duration >= 7;

select title, rating, rental_duration
from film
where (rating='G' and rental_duration >= 7)
	or (rating='PG-13' and rental_duration < 4);
	
# Group by절과 Having 절 --------------------------------------------------
# where : 그룹화 하기 전 필터링 조건
# having : 그릅화 이후에 수행되는 조건

select c.first_name, c.last_name, count(*)
from customer as c
inner join rental as r
on c.customer_id = r.customer_id
group by c.first_name, c.last_name
having count(*) >= 40;

# count(*) : 그룹화 한 전체 행의 수

# Order by
select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from customer as c
	inner join rental as r 
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by c.last_name, c.first_name asc;
# 조건이 여러개인 경우, 왼쪽 조건부터 우선순위 두면서 정렬됨

# 연습문제
# 1)
select actor_id, first_name, last_name
from actor
order by last_name, first_name;

# 2)
select actor_id, first_name, last_name
from actor
where last_name = 'WILLIAMS' or last_name = 'DAVIS';

# 3) 중복 제거 (distinct)
select distinct customer_id
from rental
where date(rental_date) = '2005-07-05';

# 4)
select c.store_id, c.email, r.return_date
from customer as c
inner join rental as r 
on c.customer_id = r.customer_id 
where date(r.rental_date) = '2005-06-14'
order by return_date desc;
# 처음시작부터 ;까지 빈 줄 없게 다 연결해서 헤야 함!!
# -> 줄띄움 없이 들여쓰기로 깔끔히 정리해야 함


#11




