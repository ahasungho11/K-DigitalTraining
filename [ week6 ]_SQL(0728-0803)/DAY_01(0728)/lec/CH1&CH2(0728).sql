show databases;
use sakila;

select now(); # ';' : ';'전까지가 명령어다. 라고 말해 주는 것임

show character set;
# varchar을 좀 더 선호한다고 함

create database testdb;

use testdb;

create table person
	(person_id smallint unsigned,
	fname varchar(20),
	lname varchar(20),
	eye_color ENUM('br', 'bl', 'gr'),
	birth_date date,
	street varchar(30),
	city varchar(20),
	state varchar(20),
	country varchar(20),
	postal_code varchar(20),
	constraint pk_person primary key (person_id)
	);
# 테이블 껍데기만 만든 것
# 좌측에서 F5 눌러가면서 최신화하고, 테이블 만들어지면 더블클릭하면서 확인할 수도 있음
	
desc person;  # 만든 테이블 확인

create table favorite_food
(person_id smallint unsigned,
food varchar(20),
constraint pk_favorite_food primary key (person_id, food),
constraint fk_fav_food_person_id foreign key (person_id)
references person(person_id));
# 이런식으로 처음부터 모든 설정을 해서 만드는 경우는 적음.
# 일단 만들어 놓고 서서히 변경을 줌
desc favorite_food;
# fk로 연결되어 있는 것을 수정하려면 (제약 조건 비활성화 -> 테이블 수정 -> 제약 조건 활성화)

# 테이블 수
set foreign_key_checks=0;
alter table person modify person_id smallint unsigned auto_increment;
set foreign_key_checks=1;

desc person

select * from person;
select * from favorite_food;
# 테이블에 있는 전체 데이터들을 다 보는 것

insert into person
(person_id, fname, lname, eye_color, birth_date)
values (null, 'William', 'Turner', 'BR', '1972-05-27');
# auto increment로 바꿔서 기본키지만 null을 넣어도 자동으로 되는 것임

select * from person;

select person_id, fname, lname, birth_date from person;
select person_id, fname, lname, birth_date from person where lname = 'Turner';

insert into favorite_food (person_id, food)
values (1, 'pizza');

insert into favorite_food (person_id, food)
values (1, 'cookies');

insert into favorite_food (person_id, food)
values (1, 'nachos');

# insert into favorite_food (person_id, food)
# values (1, 'pizza'),(1, 'cookie'), (1, 'nachos');

desc person;

select food from favorite_food
where person_id = 1 order by food;
# where은 조건절
# order by은 정렬 조건. 기본값은 asc; (오름차순)이고 / desc; (내림차순)

insert into person 
(person_id, fname, lname, eye_color, birth_date, street, city, state, country, postal_code)
values (null, 'Susan', 'Smith', 'BL', '1975-11-02', '23 Maple St.', 'Arlington', 'VA', 'USA', '20220');

select person_id, fname, lname, birth_date from person;

update person
set street = '1225 Tremon St.',
	city = 'Boston',
	state = 'MA',
	country = 'USA',
	postal_code = '02138'
where person_id =5;

select * from person
# 데이터가 삭제되는 등의 수정이 있으면,
# auto~가 걸려있는 번호가 순번으로 조회되지 않을 수도 있음
# 조회결과 'Susan'이 id가 2인 것은 Auto_increment 때문인 것임

delete from person where person_id =1;

select * from person