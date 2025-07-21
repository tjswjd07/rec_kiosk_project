# %%
#사각형 넓이 구하는 클래스 만들기
class Square :
    def _init_(self) :
        self.square = int(input ('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1.직사각형\n2.평행사변형\n3.사다리꼴')) 

        if self. square == 1 : 
            print ('직사각형의 함수는 rect()입니다')
        
        elif self.squre == 2 : 
            print ('평행사변형 함수는 par()입니다')
        
        elif self.square == 3 : 
            print ('사다리꼴 함수는 trape()입니다')

    def rect(self):
        width, vertical = map(int, input('가로, 세로를 입력하세요. 예시 : 가로,세로\n >>>').split(','))
        area = width * vertical
        result = '직사각형의 넓이는 : ' + str(area)
        return result

    def par(self):
        bottom, height = map (int, input('밑변, 높이를 입력하세요. 예시 : 밑변,높이\n >>>').split(','))
        area = bottom * height 
        result = '평행사변형의 넓이는 :' + str(area)
        return result

    def trape(self):
        top, bottom, height = map (int, input ('윗변, 아랫변, 높이를 입력하세요. 예시 : 윗면,아랫변,높이\n >>>').split(','))
        area = (top + bottom) * height / 2
        result = '사다리꼴의 넓이는 :' + str(area)
        return result

# %%
#함수를 불러오지 않고, 원하는 사각형 타입을 넣으면 자동 실행
class Square:
    def __init__(self):
        self.square = int(input('넓이를 구할 사각형을 선택하세요:\n1.직사각형\n2.평행사변형\n3.사다리꼴\n>>> '))

        if self.square == 1:
            print(self.rect())  # 바로 계산

        elif self.square == 2:
            print(self.par())

        elif self.square == 3:
            print(self.trape())

        else:
            print('잘못된 입력입니다.')

    def rect(self):
        width, vertical = map(int, input('가로, 세로를 입력하세요 (예: 3,5):\n>>> ').split(','))
        return f'직사각형의 넓이는: {width * vertical}'

    def par(self):
        bottom, height = map(int, input('밑변, 높이를 입력하세요 (예: 4,6):\n>>> ').split(','))
        return f'평행사변형의 넓이는: {bottom * height}'

    def trape(self):
        top, bottom, height = map(int, input('윗변, 아랫변, 높이를 입력하세요 (예: 3,5,4):\n>>> ').split(','))
        return f'사다리꼴의 넓이는: {(top + bottom) * height / 2}'
    
    a = Square()


# %%



