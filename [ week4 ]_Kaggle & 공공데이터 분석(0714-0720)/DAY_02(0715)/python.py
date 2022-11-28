# 모듈 로딩
import pandas as pd
import platform

# 파일 로딩 -> DF 생성
df = pd.read_csv('subwaytime.csv')
df.head()

# 컬럼명 확인
df.columns

# 필요한 컬럼들 뽑기, 컬럼명 변경
commute_df = df.iloc[:, [1, 3, 11, 13]]
commute_df.drop(0, inplace=True)
commute_df = commute_df.rename({'Unnamed: 11':'7-8 하차', 'Unnamed: 13':'8-9 하차'},axis='columns')
commute_df
#
# # 컬럼의 데이터 타입 확인 : object -> int로 바꾸자 (연산해야함)
# commute_df.dtypes
#
# # 데이터 타입 바꾸기
# commute_df['7-8 하차'] = commute_df['7-8 하차'].astype('int64')
# commute_df['8-9 하차'] = commute_df['8-9 하차'].astype('int64')
# commute_df.dtypes
#
# # 멀티 인덱스 문제로 숫자와 문자가 섞여 있는 'object'였어서 형변환이 안됐었음 -> 해당 행 삭제 -> 한 컬럼 문자열만 있는 object만든 후 변환


# #####
# max_num_list = [0] * 7
# max_station_list = [''] * 7
#
# for i in range(8):  # 만들어진 배열에 넣기 쉽게끔 0부터
#     line_str = '{}호선'.format(i + 1)  # 호선 숫자는 맞춰야 하니까 +1
#     commute_df = commute_df[commute_df['호선명'] == line_str]
#
#     row_sum_df = commute_df.sum(axis=1)
#     # df의 해당 행(가로)의 합 (axis=1 이기 때문)
#
#     #     list1[i] =
#     passenger_list = row_sum_df.to_list()
#
#     # 호선 구분 전, 각 행의 합들이 모여 있는 해당 열에서 최대값 찾기
#     max_number = row_sum_df.max(axis=0)
#     max_num_list[i] = max_number
#
#     row_sum_df.idxmax()
#     max_index = row_sum_df.idxmax()
#     max_line, max_station = df.iloc[max_index, [1, 3]]  # [1]: 호선,[3]: 지하철역명 // 원본 DF인 df에서 수행해야 함
#     max_station_list[i] = max_station
#
#     print('출근 시간대 {0} 최대 하차역은 {1}역이고 하차인원은 {2:,}명 입니다.'.format(max_line, max_station, max_number))