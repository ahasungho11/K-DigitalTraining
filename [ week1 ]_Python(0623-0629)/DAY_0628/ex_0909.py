
#---------------------------------------------------------------------------------------------------------------
# 벽돌깨기 프로그램 만들기
#---------------------------------------------------------------------------------------------------------------
nickname = ''
level = 0
score = 0
ranking = 0

# nickname2 = ''
# level2 = 0
# score2 = 0
# ranking2 = 0

# 유저가 늘어난다면 3, 4 계속 늘려나가야 함
# => 문자, 정수 형태의 변수들 4개 set가 유저1명을 표시하는 것 => 메모리 생성하면서 계속 만들게 되는 셈
# => 플레이어의 정보를 다 갖고 있는 1개의 변수로 만들고 이것을 참조할 수 있다면, 새로운 타입을 만드는 것이 좋음
# ex) player라는 data type을 만들어서  nickname(문자), level/score/ranking(정수) 를 묶어서 쓰겠다

player1 = None
player2 = None

class player:

# 최초로 입력할 떄는 닉네임 하나만 받아도, 이어서 하는 경우 4개다 받아도 작동하도록 초깃값을 입력해야 함

    def __init__(self, nickname, level=0, score=0, ranking=0):
        self.nickname = nickname
        self.level = level
        self.score = score
        self.ranking = ranking


    # 클래스의 인스턴스 변수들의 값을 업데이트 또는 읽기 하는 메서드
    # set메서드 - get메서드 (인스턴스의 값을 넣어주는 메서드, 현재 인스턴스의 값을 읽어주는)
    # 젤 첨에는 이름만 입력 받을 거니까

    def setlevel(self, level):
        self.level = level

    def setscore(self, score):
        self.score = score

    def setranking(self, ranking):
        self.ranking = ranking

    def setupdate(self, level, score, ranking):
        self.level = level
        self.score = score
        self.ranking = ranking

    def getnickname(self):
        return self.nickname

    def getlevel(self):
        return self.level

    def getscore(self):
        return self.score

    def getranking(self):
        return self.ranking


# 게임하는 사람의 정보 입력 받기
# 함수명 : setPlayer
# 파라미터 : 없음
# 반환값 : 없음

def setPlayer():
    # nickname, level, score, ranking = input('닉네임 : ').split(',')
    # lever = 0
    # score = 0
    # ranking = 0
    global player, player2
    nickname = input('닉네임 :')
    if player1 == None:
        player1 = player(nickname)
    else:
        player2 = player(nickname)



#---------------------------------------------------------------------------------------------------------------
# 메뉴 출력하기
# 함수명 : displayMenu
# 파라미터 : 없음
# 반환값 : 없음
#---------------------------------------------------------------------------------------------------------------

def displayMenu():
    print('1. 회원가입')
    print('2. 게임시작')
    print('3. 랭킹보기')
    print('4. 종   료')

def playGame():
    level = 3
    score = 1021
    ranking = 2

# 프로그램코드-------------------------------------------------------------------------------------------------------
while True:
    displayMenu()
    select = input('메뉴 선택 : ')
    if select == '4' :
        #파일에 기록하고 종료
        
        break

    elif select == '1':
        setPlayer()

    elif select == '2':
        playGame()
#-----------------------------------------------------------------------------
# 변수의 스코프
# 지역변수 : 함수에서만 사용, 파라미터, 함수안에 변수들
# 전역변수 : 파이썬 파일 안에 있는 변수, 같은 파이썬 파일안에 있는 함수에서 사용 가능

