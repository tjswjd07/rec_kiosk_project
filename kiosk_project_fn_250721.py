# %%
#사전 데이터 입력
                                                        #시간을 나타내기 위해 가져오는 라이브러리 
from datetime import datetime 


menu = [                                               #메뉴 딕셔너리리 2차원으로 나타내기 ([메뉴명, 가격]) > 메뉴명과 가격 짝을 지어줘서 헷갈리지 않고 좀 더 직관적
    {'name': 'americano', 'price': 2000},
    {'name': 'latte', 'price': 3000},
    {'name': 'mocha', 'price': 3000},
    {'name': 'yuza_tea', 'price': 2500},
    {'name': 'green_tea', 'price': 2500},
    {'name': 'choco_latte', 'price': 3000}
]

                                                        #데코레이터 함수 정의
def receipt_decorator(func):
    def wrapper(self):
        print('⟝' + '-' * 60 + '⟞')
        print('|{:^61}|'.format('SJ cafe 주문 영수증'))
        print('|{:^61}|'.format(f"주문일시: {self.order_time.strftime('%Y-%m-%d %H:%M:%S')}"))
        print('|' + ' ' * 61 + '|')
        func(self)  # 원래 table() 실행
        print('|' + ' ' * 61 + '|')
        print('|{:^61}|'.format('♥ 행복하세요 ♥'))
        print('⟝' + '-' * 60 + '⟞')
    return wrapper




#키오스크 클라스 만들기

class Kiosk:
                #생성자 속성 정의 (menu = name, price)
        def __init__(self):                 
            self.menu = menu 
        
        
         #메뉴 출력 메서드
        def menu_print(self):              
            for i, item in enumerate(self.menu, start =1):
                print(i, item['name'], ':', item['price'], '원')    #1부터 시작하는 메뉴를 하나씩 번호를 붙여 꺼내줌
        
         #메뉴 선택 메서드
        def menu_select(self):              
            self.order_menu = []            #고객이 실제로 주문한 항목들을 담는 주문 내역 저장소 != 그냥 주문 가능한 리스트 self.name과는 다른 것
            self.order_price = []

            n = 0                                   #메뉴선택 시 기초값 (필요)
            while n < 1 or len(self.menu) < n:      #유효한 값을 입력할 때까지 반복
                n = int(input("음료 번호를 입력하세요 : "))
                if 1 <= n <= len(self.menu):        #제대로 된 값을 입력한 경우
                    pass
                else: 
                    print("없는 메뉴입니다. 다시 주문해 주세요")  #잘못된 값을 입력한 경우
            
            t = 0               #온도 선택 시 기초값 (필요)
            while t != 1 and t !=2 : #유효한 값을 입력할 때까지 반복
                t = int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
                if t == 1:
                    self.temp = "HOT"
                elif t == 2: 
                    self.temp = "ICE"
                else: 
                    print("1과 2중 하나를 입력하세요\n")
            
            self.order_menu.append(self.temp + ' ' + self.menu[n-1]['name'])  #주문메뉴를 온도 + 메뉴명 형태로 계속해서 업데이트
            self.order_price.append(self.menu[n-1]['price'])   #주문 가격을 계속해서 업데이트
            print('주문음료', self.temp, self.menu[n-1]['name'], ':', self.menu[n-1]['price'], '원')

            while n !=0:   #0을 통해 주문 종료하기 전까지 추가 주문
                print()     #줄바꿈
                n = int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요 : "))
                if 1 <= n <= len(self.menu):   #메뉴를 주문한 경우
                    t = 0
                    while t !=1 and t != 2:     #온도 선택 설문 다시
                        t = int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))

                    if t == 1:
                        self.temp = 'HOT'
                    elif t == 2: 
                        self.temp = "ICE"
                    else: 
                        print("1과 2중 하나를 입력하세요\n")   
                     
                    self.order_menu.append(self.temp + ' ' + self.menu[n - 1]['name'])
                    self.order_price.append(self.menu[n - 1]['price'])

                    print('추가 주문 음료', self.temp, self.menu[n - 1]['name'], ' : ', self.menu[n - 1]['price'], '원\n', '합계 : ', sum(self.order_price), '원')

                else:
                    if n == 0:
                        print("주문이 완료되었습니다\n")
                        self.order_time = datetime.now()     #주문 완료되었을 때 그 시점의 시간 저장

                        for i in range(len(self.order_price)):                          
                            print(f"{self.order_menu[i]} : {self.order_price[i]} 원")        #최종 주문내역 출력
                        
                        print(f"\n총합 : {sum(self.order_price)} 원")
                    
                    else:
                        print("없는 메뉴입니다. 다시 주문해주세요")
        #pay 메서드
        def pay(self):
            p = 0
            while p != 1 and p != 2:
                p = int(input("지불수단을 선택해 주세요. 현금은 1번, 카드는 2번을 눌러주세요: "))
                if p == 1:
                    print("직원을 호출하겠습니다.")
                elif p == 2:
                    print("IC칩 방향에 맞게 카드를 꽂아주세요.")
                else:
                    print("1과 2중 하나를 입력하세요\n")
        
        #영수증 출력 메서드
        @receipt_decorator
        def table(self):
            for i in range(len(self.order_menu)):
                print(f"{self.order_menu[i]} : {self.order_price[i]} 원")
            print(f"\n합계: {sum(self.order_price)} 원")


# %%
k = Kiosk()
k.menu_print()
k.menu_select()
k.pay()
k.table()


