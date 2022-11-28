'''
    과제 1번. 대구 기온 분석
'''
import csv
import matplotlib.pyplot as plt
import platform

def draw_two_plots(title, x_data, min_list, y_label1, max_list, y_label2):
    '''
        x_data: 연도(1991~2020)
        min_list: 최저 기온 리스트
        max_list: 최고 기온 리스트
    '''
    if (platform.system() == 'Windows'):
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic')

    plt.rcParams['axes.unicode_minus'] = False # 음수(-)가 깨지는 현상 방지
    plt.figure(figsize=(18, 4))
    plt.plot(x_data, min_list, marker='s', markersize=6, color='b', label=y_label1)
    plt.plot(x_data, max_list, marker='s', markersize=6, color='r', label=y_label2)
    plt.xticks(x_data)  # 모든 xtick값을 출력함
    # plt.yticks([0, 10, 20, 30, 40]) # 모든 yticks 값을 출력함
    plt.title(title)
    plt.legend()
    plt.show()

def display_temp_list(title, temp_list):
    count = len(temp_list)
    print(title)
    for i in range(count):
        if(i <= count-2):
            print("%.1f" % temp_list[i], end=', ')
        else:
            print("%.1f" % temp_list[i])
        if(i+1) % 10 == 0:
            print()

def average_min_max_temperature(start_year, end_year, target_month):
    period = (end_year - start_year) + 1  # 기온 분석 기간

    # 최저 기온 값을 계산하기 위한 array
    min_month_list = [0] * period  # 입력된 기간 동안의 해당 월의 최저기온 값의 평균 저장
    min_count_list = [0] * period
    avg_min_month_list = [0] * period

    # 최고 기온 값을 계산하기 위한 array
    max_month_list = [0] * period  # 입력된 기간 동안의 해당 월의 최고기온의 평균 저장
    max_count_list = [0] * period
    avg_max_month_list = [0] * period

    f = open('daegu_utf88.csv', 'r', encoding='utf-8')
    '''
    | 날짜 | 지점 | 평균기온 | 최저기온 | 최고기온 |
      [0]   [1]    [2]     [3]      [4]
        
    '''
    data = csv.reader(f, delimiter=',')
    next(data)

    for row in data:
        if row[4] == '' or row[3] == '': # 해당 데이터가 없는 경우 건너뜀
            continue

        date_str = row[0].split('-') # 1991.1.10 형태로 점(.)을 기준으로 분리함
        year = int(date_str[0])
        month = int(date_str[1])
        if (year >= start_year and year <= end_year):
            if(month == target_month):
                min_month_list[year-start_year] += float(row[3]) # 특정년도의 특정월의 최저 기온 값을 모두 더함
                min_count_list[year-start_year] += 1
                max_month_list[year-start_year] += float(row[4])  # 특정년도의 특정월의 최고 기온 값을 모두 더함
                max_count_list[year-start_year] += 1

    f.close()

    #display_temp_list(max_month_list)
    for i in range(len(max_count_list)):
        min_count = min_count_list[i]
        avg_min_month_list[i] = round(min_month_list[i] / min_count, 1)
        max_count = max_count_list[i]
        avg_max_month_list[i] = round(max_month_list[i] / max_count, 1)


    display_temp_list("최저기온 평균", avg_min_month_list)
    display_temp_list("최고기온 평균", avg_max_month_list)

    x_ticks = list(range(start_year, end_year+1))
    print(x_ticks)

    y_label1 = '최저기온'
    y_label2 = '최고기온'

    title = format("{0}년부터 {1}년까지 {2}월의 기온 변화".format(start_year, end_year, target_month))
    print(title)

    draw_two_plots(title, x_ticks, avg_min_month_list, y_label1, avg_max_month_list, y_label2)
    #draw_plot(x_ticks, avg_month_list, title)

def main():
    start_year = int(input('시작 연도를 입력하세요: '))
    end_year = int(input('마지막 연도를 입력하세요: '))
    month = int(input("기온 변화를 측정할 달을 입력하세요: "))

    average_min_max_temperature(start_year, end_year, month)

main()

