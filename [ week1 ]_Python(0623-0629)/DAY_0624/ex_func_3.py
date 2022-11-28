year = 2022


def printYear():
    print(f'올해는 {year}')


if __name__ == '__main__':
    for i in range(5):
        printYear()

print(f'[ex_func_3]__name__ => {__name__}')

# 다른 파이썬 파일에서 자동으로 쓰이는 것 방지하기 위해
# 앞뒤로 __가 붙어 있는 경우 =>


#==============


# for i in range(5):
#     printYear()
#
# print(f'[ex_func_3]__name__ => {__name__}')

