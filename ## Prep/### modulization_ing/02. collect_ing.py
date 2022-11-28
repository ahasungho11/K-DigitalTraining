# ---------------------------------------------------------------------------------------------------------
# 1. enumerate함수 활용 ( 인덱스번호와 데이터 함께 출력 )
# ---------------------------------------------------------------------------------------------------------

datas = [total_fashion_cloth, total_fashion_acc, total_makeup]
data_names = ['패션의류', '패션잡화', '화장품/미용']

for i, data in enumerate(datas):
    print(f'''
{data_names[i]}    -----------------
index :
{data.index}

columns :
{data.columns}

na :
{data.isna().sum()}
    ''')

