import pandas as pd

hollys_branches = pd.read_csv('hollys_branches.csv', encoding= 'utf-8')
hollys_branches

# 검색어를 공백 단위로 분할
search_str = input('검색할 매장의 도시를 입력하세요:').split()

# 분할한 검색어를 모두 포함하는지 판단하는 조건생성
cond= [True] * (hollys_branches.shape[0])
print(type(cond))

for s in (search_str):
    cond = cond * hollys_branches['주소'].str.contains(s)

print(cond)
print(len(cond))