# # 복사본 파일에 데이터 쓰기
# filename = 'home.html'
# data = filename.split('.')+'.txt'
# print(data)
# print(f'{data[0]}')
# print(filename.split('.')[0])

# filename = './html/home.html'
# print(f'filename의 인덱스 => {filename[:filename.rindex(".")]}')

def fileCopy(filename):
    # 원본 파일 열고 데이터 꺼내기
    srcFile = open(filename, mode= 'r', encoding='utf-8')
    data = srcFile.read()
    srcFile.close()

    # 복사본 파일에 데이터 쓰기
    filename = filename[:filename.rindex(".")] + '.txt'
    # data = filename.split('.')+'.txt'
    desFile = open(filename, mode = 'w', encoding='utf-8')
    desFile.write(data)
    desFile.close()

fileCopy('./html/home.html')


# html 문서의 객체화 ->