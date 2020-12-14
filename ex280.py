import random # 랜덤계좌번호 부여를 위한 random 모듈

class Account: # Accoun 클래스 만들기

    accCount = 0 # 총 계좌의 갯수를 세는 클래스 변수

    def __init__(self, holder, balance): # 생성자를 생성하고, 입력 받아야 할 두 메서드를 지정한다.
        self.holder = holder # 예금주
        self.balance = balance # 잔액
        self.bankName = 'SC 은행' # 은행이름
        self.accNum = str(random.randrange(100, 999)) + '-' + str(random.randrange(10, 99)) + '-' + str(random.randrange(100000, 999999)) # 000-00-000000 형태로 랜덤한 값의 계좌번호를 str 의 자료형으로 생성.
        
        self.depositLog = [] # 입금기록 저장용 리스트
        self.withdrawLog = [] # 출금기록 저장용 리스트


        Account.accCount += 1 # 계좌가 하나 추가로 생성될 때 마다 accCount 값이 1씩 증가한다.
    
    def get_account_num(self): # 총 계좌의 갯수를 출력하는 클래스 변수
        print(self.accCount)

    def deposit(self, amount): # 입금 메서드, 입금은 최소 1원 이상일때 가능.
        self.amount = amount
        if amount >= 1:
            self.balance += amount

            self.depositLog.append(amount) # 입금기록 depositLog 에 추가

        
        
    def withdraw(self, amount): # 출금 메서드, 출금은 최대 잔고만큼 가능.
        self.amount = amount 
        if amount <= self.balance:
            self.balance -= amount

            self.withdrawLog.append(amount) # 출금기록 withdrawLog 에 추가


    def deposit_history(self): # 입금기록을 출력하는 메서드.
        print(self.depositLog)
        
    def withdraw_history(self): # 출금기록을 출력하는 메서드.
        print(self.withdrawLog)




young = Account('junyoung', 100)
ha = Account('junha', 140)
yang = Account('hyunmi', 80)
jang = Account('sooho', 200)


ha.deposit(50)

ha.withdraw(70)

ha.deposit(20)

ha.withdraw(40)

ha.deposit(90)


ha.deposit_history()
ha.withdraw_history()


