prompt = '''
=== 나의 주소록 ===
  1. 전 체 보 기
  2. 검      색
  3. 추      가
  4. 종      료
================='''

number = 0
while number != 4:
    print(prompt)
    choice = int(input('메뉴 선택 : '))
    if choice == 4:
        break

    filename = '이름_전화번호.txt'

    if choice == 3:
        file = open(filename, mode='a', encoding='utf-8')
        data = input('이름, 전화번호, 지역을 입력하세요 : 예시) 홍길동_1234_부산 ')

        file.write(data)
        file.write('\n')
        file.close()

# Q1) 문제 설명을 하실 때 놓쳐서인지, [ mode = 'w' ] 로 해서 .txt 파일을 생성하면서 만드는 방법을 잘 모르겠습니다.
#     - 일단 되는대로 파일 1개 만들어서 검색하는 것으로 만들기는 했습니다.

    if choice == 1:

        file = open(filename, mode='r', encoding='utf-8')

        data = file.readlines()
        file.close()
        print('\n전체 보기')
        for i in data:
            print(f'{i[:i.rindex("_")]}')

    if choice == 2:
        name = input("검색 단어: ")

        file = open(filename, mode='r', encoding='utf-8')
        data = file.readlines()
        file.close()

        for i in data:
            if name in i:
                print(f'파일명: {i[:i.rindex("_")]}')
                print(f'{" ".join(i.split("_"))}')