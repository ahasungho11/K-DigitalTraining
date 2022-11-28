#### 모듈 읽어오기
import os
import csv
import pandas as pd
import warnings
warnings.simplefilter("ignore")
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------------

# 이렇게 하는 것을 줄여
# 바꿔주어야 할 것 : 1~7 / 파일명
# df1 = pd.read_csv(DIR + 'comedy_view_top.csv', index_col=0)
# df2 = pd.read_csv(DIR + 'entertainment_view_top.csv', index_col=0)
# df3 = pd.read_csv(DIR + 'film_view_top.csv', index_col=0)
# df4 = pd.read_csv(DIR + 'sports_view_top.csv', index_col=0)
# df5 = pd.read_csv(DIR + 'travel_view_top.csv', index_col=0)
# df6 = pd.read_csv(DIR + 'vehicles_view_top.csv', index_col=0)
# df7 = pd.read_csv(DIR + 'vlog_view_top.csv', index_col=0)

#---------------------------------------------------------------------------------------
# case 1) for문으로 변수 선언하기 : globals() 활용
#---------------------------------------------------------------------------------------
# => globals()['변수명'.format(변수 이름마다 부여할 값)] = 변수에 입력할 값
# => globals()는 딕셔너리 형태
# => globals()['변수명'] 을 하면 해당 변수에 들어간 value값을 읽어올 수 있음
# 아래에서 실험해 봤듯이, globals()를 활용해 여러개의 변수들을 돌려도 모두 전역함수로 변수를 선언한 것처럼 다 쓸 수 있음!!!

DIR = './exam/'
os.listdir(DIR)

for file in range(len(os.listdir(DIR))):
    globals()['df{}'.format(file+1)] = pd.read_csv( DIR + os.listdir(DIR)[file], index_col=0 )
    # print(file+1, ":", '\n', globals()['df'+ str(file+1)])

for i in range(0, 10):
    globals()["s{}".format(i)] = i
    # print(i, ":", '\n', globals()['s'+str(i)])

print(df1)
print(s1)

#---------------------------------------------------------------------------------------
# case 1-1) 번외 : DF의 컬럼들을 편집할 때 for문 쓰기
#---------------------------------------------------------------------------------------

for i in range(7):
    globals()['df{}'.format(i+1)]['조회수'] = globals()['df{}'.format(i+1)]['조회수'].str.replace(',', '')
    globals()['df{}'.format(i+1)]['조회수'] = globals()['df{}'.format(i+1)]['조회수'].astype('int64')

# df1['조회수']=df1['조회수'].str.replace(',', '')
# df1['조회수']=df1['조회수'].astype('int64')
# df2['조회수']=df2['조회수'].str.replace(',', '')
# df2['조회수']=df2['조회수'].astype('int64')
# df3['조회수']=df3['조회수'].str.replace(',', '')
# df3['조회수']=df3['조회수'].astype('int64')
# df4['조회수']=df4['조회수'].str.replace(',', '')
# df4['조회수']=df4['조회수'].astype('int64')
# df5['조회수']=df5['조회수'].str.replace(',', '')
# df5['조회수']=df5['조회수'].astype('int64')
# df6['조회수']=df6['조회수'].str.replace(',', '')
# df6['조회수']=df6['조회수'].astype('int64')
# df7['조회수']=df7['조회수'].str.replace(',', '')
# df7['조회수']=df7['조회수'].astype('int64')

#---------------------------------------------------------------------------------------
# case 2) df에 담겨 있는 것을 인덱스 번호를 이용해 꺼내서 필요한 이름으로 선언하여 사용
#---------------------------------------------------------------------------------------

DIR = './exam/'
os.listdir(DIR)
print(os.listdir(DIR))

df = []
for file in os.listdir(DIR):
# print(file, type(file))
    df.append(pd.read_csv( DIR + file, index_col=0 ))

# 0번 인덱스에 들어가있는 'comnedy_view_top.csv'에 들어가 있는 내용을 df1에 선언하는 것
df1 = df[0]
print(df1)

#---------------------------------------------------------------------------------------
# case 3) append를 활용해서 for문으로 파일 읽기   =>  os.listdir로 case 1)처럼 하면 되니까 요건 안쓸 듯
#---------------------------------------------------------------------------------------

# 파일 경로
DIR = './Data_1/'
FILE_ = [ DIR+'tving_movie_M.xlsx', DIR+'tving_movie_F.xlsx', DIR+'tving_drama_M.xlsx',
         DIR+'tving_drama_F.xlsx', DIR+'tving_animation_M.xlsx', DIR+'tving_animation_F.xlsx',
         DIR+'tving_entertainment_M.xlsx', DIR+'tving_entertainment_F.xlsx' ]


# 파일 로딩 -> DF 저장
df =[]
for i in FILE_:
    df.append( pd.read_excel({i}, skiprows=6))

# df에 모두 들어있기 때문에 각 파일을 인덱스 번호로 불러내서 새로운 변수로 선언을 하든지 하면서 꺼내서 사용할 것!!

#---------------------------------------------------------------------------------------
# case 4) 번외. os.listdir을 활용하여 DF를 concat하고, 편집하는 등의 skill
#---------------------------------------------------------------------------------------

# 파일 통합을 위해 쪼개진 파일을 담아 놓은 폴더
DEAGU_DIR_PATH = './문화공연/대구_공연행사/'
SEOUL_DIR_PATH = './문화공연/서울_공연행사/'

# 쪼개진 파일을 읽어 통합한 DF를 파일로 정리해서 보낼 폴더
DIR_PATH = './문화공연/공연'

# 쪼개진 파일명 읽기 위한 os.listdir
os.listdir(DEAGU_DIR_PATH)
os.listdir(SEOUL_DIR_PATH)

# 0번 파일을 읽음 (모두 동일한 양식임을 확인한 상태) (for 컬럼명을 따기 위해서)
deagu_show = pd.read_csv(DEAGU_DIR_PATH + os.listdir(DEAGU_DIR_PATH)[0] )
seoul_show = pd.read_csv(SEOUL_DIR_PATH + os.listdir(SEOUL_DIR_PATH)[0] )

# 위에서 읽은 0번 파일의 컬럼명들만 따서 가로 행(하나의 시리즈)를 만들고
# 이어서 (0번 파일을 포함한 모든 파일들을 인덱스를 무시하고 모두 concat으로 붙여버리기)

# deagu_show_total = pd.DataFrame(columns = deagu_show.columns)
for file in os.listdir(DEAGU_DIR_PATH):
    deagu_show = pd.read_csv(DEAGU_DIR_PATH + file)
    deagu_show_total = pd.concat([deagu_show_total, deagu_show], ignore_index= True)

seoul_show_total = pd.DataFrame(columns = seoul_show.columns)
for file in os.listdir(SEOUL_DIR_PATH):
    seoul_show = pd.read_csv(SEOUL_DIR_PATH + file )
    seoul_show_total = pd.concat([seoul_show_total, seoul_show], ignore_index= True)

# ---------------------------------------------------------------------------------------------------------
# case 4-1) 번외. os.listdir을 활용하여 DF를 concat하고, 편집하는 등의 skill
# ---------------------------------------------------------------------------------------------------------

import pandas as pd
import os

DATA_PATH = './fc_fa_m_data/'
os.listdir(DATA_PATH)
print(os.listdir(DATA_PATH))

test = pd.read_csv(DATA_PATH + os.listdir(DATA_PATH)[0], skiprows=10, index_col=0)
print(test)
print(test.head(2))

# 분류별로 각 DataFrame 만들기
total_fashion_cloth = pd.DataFrame(index=test.index)
total_fashion_acc = pd.DataFrame(index=test.index)
total_makeup = pd.DataFrame(index=test.index)

# 읽은 csv파일 1개로 DF를 만들었고, 이 1개의 DF(file)의 컬럼들을 꺼내쓰는 것이므로 file 변수 하나로 써도 되는 것
for file_name in os.listdir(DATA_PATH):
    file = pd.read_csv(DATA_PATH + file_name, skiprows=10, index_col=0)

    # 각 데이터 프레임에 성별_나이별 자료 추가
    total_fashion_cloth.insert(0, file_name.split('.')[0], file[['패션의류']])
    total_fashion_acc.insert(0, file_name.split('.')[0], file[['패션잡화']])
    total_makeup.insert(0, file_name.split('.')[0], file[['화장품/미용']])

# ---------------------------------------------------------------------------------------------------------
# case 4-2) 번외. for문과 to_csv ( csv파일로 저장 )
# ---------------------------------------------------------------------------------------------------------

for i in range(3):
    datas[i].to_csv('./naver_shopping/'+data_names[i].replace('/','_')+'.csv')

# -----------------------------------------------------------------------------------------------------------

