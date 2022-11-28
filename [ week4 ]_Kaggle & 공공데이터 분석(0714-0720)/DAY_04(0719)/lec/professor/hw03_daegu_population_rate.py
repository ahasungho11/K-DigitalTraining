'''
 과제 3. 대구시 각 구별 남녀 비율을 파이 차트로 표현
 대구의 각 구별 남여 성비율 조사
    - 중구, 동구, 서구, 남구, 북구, 수성구, 달서구, 전체
'''

import csv
import matplotlib.pyplot as plt
import platform

def draw_pie_charts(city, gender_dict):
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic', size=8)
    gender_type = ['남성', '여성']

    i = 1
    fig, axes = plt.subplots(2, 4, figsize=(10, 8))
    fig.suptitle('{} 구별 남녀 인구 비율'.format(city), fontsize=20)
    for key in gender_dict:
        plt.subplot(2, 4, i)
        plt.title(key, size=10)
        values = gender_dict.get(key)
        plt.pie(values, labels=gender_type, autopct='%.1f%%', startangle=90)
        i += 1

    #plt.tight_layout()
    plt.show()

def calculate_population_rate():
    f = open('gender.csv', encoding='euc_kr')
    data = csv.reader(f)
    header = next(data)
    gender_dict = dict()
    gender = ['남성', '여성']
    city = '대구광역시'

    total_male_count = 0 # 도시의 남성 인구수
    total_female_count = 0 # 도시의 전체 여성 인구수
    gu_label = ['중구', '동구', '서구', '남구', '북구', '수성구', '달서구', '전체']

    location = city +""
    i = 0

    for row in data:
        if city in row[0]:
            #if(first):
            if location == '대구광역시':
                total_male_count = int(row[104].replace(',', ''))
                total_female_count = int(row[207].replace(',', ''))
                print('대구광역시 전체 남성인구: {:,}, 전체 여성인구: {:,}'.
                                format(total_male_count, total_female_count))

            if i < len(gu_label) - 1:
                location = city + ' ' + gu_label[i] # '대구광역시 중구'
                if location in row[0]:
                    male_count = int(row[104].replace(',', ''))
                    female_count = int(row[207].replace(',', ''))
                    gender_dict[location] = [male_count, female_count]
                    i += 1
                    continue
            else:
                break

    f.close()
    location = city + ' ' + gu_label[7]
    gender_dict[location] = [total_male_count, total_female_count]
    print(gender_dict)
    draw_pie_charts(city, gender_dict)

calculate_population_rate()