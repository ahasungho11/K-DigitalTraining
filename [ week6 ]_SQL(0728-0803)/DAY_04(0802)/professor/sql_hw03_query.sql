/*
 *  과제 3번 Query 
 * 
 */

use shoppingmall;

# 
# user_table과 buy_table 을 내부 조인 
select * 
from buy_table inner join user_table
on buy_table.userID = user_table.userID; 

# 1번. 내부 조인한 결과에 '연락처' 컬럼 추가 
select user_table.userName, buy_table.prodName, user_table.addr,
	concat(user_table.mobile1, user_table.mobile2) as '연락처'
from buy_table inner join user_table 
on buy_table.userID = user_table.userID; 

# 2번 내부 조인한 다음, userID값이 KYM이 구매한 물건과 회원 정보 출력  
select b.userID, u.userName, b.prodName, u.addr, concat(u.mobile1, u.mobile2) 
from buy_table as b 
    inner join user_table as u
on b.userID = u.userID 
where b.userID = 'KYM';


# 특정 groupName(분류)를 구매한 회원 검색 


# 특정 prodName(물품)을 구매한 회원 검색 


# 3번. 전체 회원이 구매한 목록 모두 출력 (회원 아이디 순으로 정렬)
select u.userID, u.userName, b.prodName, u.addr, concat(u.mobile1, u.mobile2) as 연락
from user_table as u 
    inner join buy_table as b 
    on u.userID = b.userID 
order by u.userID;

# 4번. 쇼핑몰에서 한 번이라도 구매한 기록이 있는 회원 정보 출력 
select distinct u.userID, u.userName, u.addr 
from user_table as u 
    inner join buy_table as b 
    on u.userID = b.userID 
order by u.userID;

# 5번. 특정 지역에 거주하는 회원 명단 출력 
select u.userID, u.userName, u.addr, concat(u.mobile1, u.mobile2) as 연락
from user_table as u 
    inner join buy_table as b 
    on u.userID = b.userID 
where u.addr = '경북' or u.addr = '경남'
order by u.userID;




