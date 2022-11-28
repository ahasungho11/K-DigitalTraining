# 0729_오후)

# 조건 평가

use sakila;

# where 절
where first_name = 'STEVE' and create_date > '2006-01-01'
where first_name = 'STEVE' or create_date > '2006-01-01'

# 두 조건을 합친다면 
where (first_name = 'STEVE' or last_name = 'YOUNG')
and create_date > '2006-01-01'

# not 연산자
where not (first_name = 'STEVE' or last_name = 'YOUNG')
and create_date > '2006-01-01'

where first_name <> 'STEVE' and last_name <> 'YOUNG'
and create_date > '2006-01-01'



# 동등 조건 : '열 = 표현/값1'
select c.email
from customer as c

on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14';
#               열              값1

# 부등 조건 : 두 표현이 동일하지 않음
# <> or != 사용
select c.email
from customer as c
on c.customer_id = r.customer_id
where date(r.rental_date) <> '2005-06-14';


# -------------------------------------------------------------------------------

# date함수를 써야 일반적으로 생각하는 해당 일자 ~23:59:59까지의 자료를 뽑아냄
# cf) 앞서 봤던 rental_date 자체로 하면 사실상 하루 전날의 23:59:59까지 나온다는 것!
# cf) 만약 between으로 쓰면 원하는 대로 나오겠징
# => 결국 
# -> 구분해서 잘 쓸 것


# between 잘 쓸 것
# 범위의 하한값/ 하한값 모두 '='이 들어가는 셈. 포함됨!!

# 명확하게 날짜'만' 뽑아서 정확하게 비교하려면 
# where date(rental_date) between '2005-06-14' and '2005-06-16';
# -> date()를 씌워주는 것이 좋음


# 문자열 범위 => 사전식으로 생각하면 됨
select last_name, first_name
from customer
where last_name between 'FA' and 'FRB'


# 멤버십 조건
# OR 또는 IN() 연산 => 파이썬에서 썼던 in과 같은 기능을 한다고 보면 됨
# 유한한 값의 집합으로 제한

select title, rating
from film
where rating='G' or rating='PG';

# <=>  둘다 같은 결과가 나옴

select title, rating
from film
where rating in ('G', 'PG');

# %의 위치에 따라 조건이 다를 수 있음!!
select title, rating
from film
where rating in (select rating from film where title like '%PET%');

# select 절만 떼어내서 보면 아래와 같은 것이지
select title, rating from film where title like '%PET%';

# -> 즉 where절의 내용은 아래와 같이 된다는 것
select title, rating from film where rating in ('G', 'PG')


# not in 사용
select title, rating
from film
where rating not in ('R', 'NC-17', 'PG-13');

select title, rating
from film
where rating in ('R', 'NC-17')


# 일치 조건
select left('abcdefg' ,3)
select mid('abcdefg' ,2,3)
select right('abcdefg' ,3)

# 와일드 카드
# '_' : 정확히 한 문자 (underscore)
# '%' : 개수에 상관없이 모든 문자 포함
# 사용시 like 연산자를 사용

select last_name, first_name
from customer
where last_name like '_A_T%S';
# '_A_T%S' : 두번째 A, 네번째 T, 마지막은 S로 끝나는 문자열 (T와 S 사이의 글자수는 무관)

select last_name, first_name
from customer
where (last_name like 'Q%') or (last_name like 'Y%');

# 정규 표현식 사용 : regexp
select last_name, first_name
from customer
where last_name regexp '^[QY]'; 
# ^: 시작기호, $: 끝나는 기호, 
# ^[QY]  :  Q 또는 Y로 시작하는 단어

# Null
# 해당 사항 없음, 아직 알려지지 않은 값, 정의 되지 않은 값
# 확인 법 : is null 사용 (=null)

select rental_id, customer_id, return_date
from rental
where return_date is null;
# where return_date = null;  ->  안나오넹

select rental_id, customer_id, return_date
from rental
where return_date is not null;

# Null과 조건 조합
select rental_id, customer_id, return_date
from rental
where return_date is null
   or return_date not between '2005-05-01' and '2005-09-01';
   # =>  date()로 하지 않았기 때문에, 2005-08-31 23:59:59 까지 나온 것이기 때문에
   #     2005-09-01 00:00:00 ~ 값들이 찍혀 나오는 것임
  
# 서브셋 조건 설정
select payment_id, customer_id, amount, date(payment_date) as payment_date
from payment
where (payment_id between 101 and 120)
and (payment_id != 5) and (amount > 8 or date(payment_date) = '2005-08-23');

#
select payment_id, customer_id, amount, date(payment_date) as payment_date
from payment
where (payment_id between 101 and 120)
and (customer_id = 5) and not (amount > 6 or date(payment_date) = '2005-06-19');


 
#  해당 csv를 바로 끌어오도록






