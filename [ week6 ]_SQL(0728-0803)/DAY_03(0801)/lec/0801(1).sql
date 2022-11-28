show databases;

use sakila;

# 집합 연산 규칙
- 두 데이터셋 모두 같은 수의 열(column)을 가져야 됨
- 두 데이터셋의 각 열의 자료형은 서로 동일해야 됨

* 집합 연산을 하기 전에 customer 테이블과 actor 테이블 구성 확인
-> 두 테이블 모두, first_name, last_name이 '존재'하고 '데이터타입'도 동일

 # Join
- 대부분의 쿼리는 여러 테이블을 필요로 하지 => join
- dBeaver의 경우, 명확하게 선으로 표시되어 있지 않음
- 일반적인 조인은 inner join (두 부분에서 공통적인 것만 가져오는 것)을 말한다 (기본값)

1) cross join(교차 조인, 데카르트 곱)
- 실제로 은 잘 사용하지 않음 => 각 테이블 행들의 곱
- 전부 붙이니까, on 조인 조건이 필요 없음

#
SELECT (조회 컬럼)
FROM 테이블명1 [CROSS] JOIN 테이블명2;

# 결합(join)의 조건 없이 모든 행을 결합
select c.first_name, c.last_name, a.address
from customer as c join address as a;

select count(*) from customer as c join address as a;


2) 내부 조인(inner join)
- 일치하지 않는 데이터는 검색하지 않음
- 공통된 항목의 정보만 가져와서 테이븰의 해당 내용들을 합침
- 공통된 게 있는가 -> on 조건 입력
- 어느 table의 데이터를 가져 올건지 select에 명시

# 
SELECT <열 목록>
FROM <기준 테이블> [INNER] JOIN <참조할 테이블>
ON <조인 조건>
[WHERE 검색 조건]

# 
select c.first_name, c.last_name, a.address
from customer as c inner join address as a
on c.address_id = a.address_id;

3) 외부조인(outer join)
 - 한쪽 테이블에만 존재하는 데이터들을 다른 테이블에 결합

4) ANSI join
 - 표준은 있지만, 프로그램마다/회사마다 조금씩 다르다
 - 이전 : where과 on의 구분 x
 - 이후 : where과 on의 구분 o
       (필터 조건) (join 조건)

# 이전
select c.first_name, c.last_name, a.address
from customer as c join address as a 
where c.address_id = a.address_id and a.postal_code = 52137;

# 이후
select c.first_name, c.last_name, a.address, a.postal_code
from customer c join address as a
	on c.address_id = a.address_id
where a.postal_code = 52137;

** 쉽게, 이해되게, 디버깅할 수 있게, 주석 잘 달면서 코드 짤 것

2. 세 개 이상 테이블 조인
- 테이블 구조를 확인해야 함

  desc city;
 
- 조인을 하기 전 어떻게 연결되어 있는지 확인해야 함.
-> 내부적으로 데이터를 합쳐서 출력하기 때문에, '조인 테이블 순서는 무관'
-> customer, address, city 테이블 입력 위치는 어디든 무관함

select c.first_name, c.last_name, ct.city
from customer as c
	inner join address as a          # customer와 address 조인
	on c.address_id = a.address_id
	join city as ct                  # address와 city 조인
	on a.city_id = ct.city_id;

3. 서브 쿼리 사용
- 서브 쿼리도 별칭을 줄 수 있음

select c.first_name, c.last_name, addr.address, addr.city, addr.district
from customer as c
	inner join
	(select a.address_id, a.address, ct.city, a.district
     from address as a
     	inner join city ct
     	on a.city_id = ct.city_id
     where a.district = 'California'
     ) as addr
on c.address_id = addr.address_id;

=> 서브쿼리(addr) 결과를 customer 테이블과 inner join
=> 쿼리 결과 : California에 거주하는 모든 고객들의 이름, 성, 주소 및 도시를 검색

3-1. 서브쿼리 내용만 출력해보면

select a.address_id, a.address, ct.city, a.district
	from address as a
     	inner join city ct
     	on a.city_id = ct.city_id
     where a.district = 'California';

** ERD 표가 중요함 (어떻게 연결되어 있는 것을 보면서 검색 가능여부를 판단할 수 있기 때문)

3-2. 테이블 재사용 (잦은 경우는 아님)
- 같은 테이블을 여러 번 사용하기 떄문에 테이블 별칭 사용

4. 

select f.title
from film as f
	inner join film_actor as fa
	on f.film_id = fa.film_id
	inner join actor as a
	on fa.actor_id = a.actor_id
where a.first_name = 'JOHN';

5. 실습

desc address;

select a1.address as addr1, a2.address as addr2, a1.city_id, a1.district
from address as a1
	inner join address as a2
# 	
where (a1.city_id = a2.city_id)
	and (a1.address_id != a2.address_id);  # 자기 자신 제외

# CH6 ------------------------------------------------------------------------
6. 집합 연산자
- mysql에서는 합o, 교x(-> 조인을 써서 하는 수밖에)
- union / union all
(중복 제거o) (중복 제거x)

** desc 컬럼명;   으로 확인을 해봐야지 집합 연산 가능 여부를 정하지

desc customer;

desc actor;

# type1은 어느 테이블에서 가져왔는지를 구분하기 위해서 별칭 준 것임
# (CUST, ACTR => 테이블 구분 용도)

1) union all

select 'CUST' as type1, c.first_name, c.last_name
from customer as c
union all
select 'ACTR' as type1, a.first_name, a.last_name
from actor as a;
# 799개

select count(first_name) from customer;
# 599개
select count(first_name) from actor;
# 200개

+ 자기 테이블을 그대로 합집합 하기

select 'ACTR' as typ, a.first_name, a.last_name
from actor as a
union all
select 'ACTR' as typ, a.first_name, a.last_name
from actor as a;
# 200+200 = 400개

2) union

select c.first_name, c.last_name
from customer as c
where c.first_name like 'J%' and c.last_name like 'D%'
union
select a.first_name, a.last_name
from actor as a
where a.first_name like 'J%' and a.last_name like 'D%';
       
3) intersect
 
4) 복합 쿼리
- 합집합 처리 -> 정렬

select a.first_name as fname, a.last_name as lname
from actor as a
where a.first_name like 'J%' and a.last_name like 'D%'
union all
select c.first_name, c.last_name
from customer as c
where c.first_name like 'J%' and c.last_name like 'D%'
# 합친 후, 정렬해야징
# 복합 쿼리의 첫 번째 쿼리에 있는 열의 이름인 'fname'와 'lname'를 써야함
order by lname, fname;

5) 집합 연산 규칙
- 위-> 아래
- 단, intersecdt 연산자는 우선 순위가 높음
- 순서 바꾸면, 6 -> 7 (개수 달라짐 확인)

select a.first_name, a.last_name
from actor as a
where a.first_name like 'J%' and a.last_name like 'D%'
union all
select a.first_name, a.last_name
from actor as a
where a.first_name like 'M%' and a.last_name like 'T%'
union
select c.first_name, c.last_name
from customer as c
where c.first_name like 'J%' and c.last_name like 'D%';

6) 실습
# 성이 L로 시작하는 모든 배우와 고객의 이름과 성을 찾는 복합 쿼리 작성
# order by 줄이 붙이면 오름차순 해주는 것 (복합쿼리 작업 후, 정렬)

select first_name, last_name
from actor
where last_name like 'L%'
union
select first_name, last_name 
from customer
where last_name like 'L%'
order by last_name;
