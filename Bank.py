class Bank:

    def __init__(self, name="user", balance=0, pin=0000):
        self.__balance = balance
        self._name = name
        self.__pin = pin

    def checkpin(self):
        p=int(input("Enter Your Pin : "))
        if self.__pin==p:
            return True
        else :
            return False
        
    def withdrow(self):
        if self.checkpin():
            a=int(input("Enter Your Amount : "))
            if a<=self.__balance and a>0:
                self.__balance-=a
                print("withdrow ",a)
            else :
                print("insaficent balance")

        else :
            print("invalid Pin")
                 

    def deposit(self):
        if self.checkpin():
            amount = int(input("Enter Your Amount : "))
            if amount >= 0:
                self.__balance += amount
                print("Deposit ", amount)
            else:
                print("Invalid Amount")
        else :
            print("invalid Pin")

    def checkBalance(self):
        if self.checkpin():
            print("Your Balance is : ", self.__balance)

acc1=Bank("kalpesh",20000,1234)
while True:
    print("enter your choice : 1. withdrow 2. deposit 3. check balance 4. exit")
    choice=int(input("Enter Your Choice : "))
    match choice:
        case 1:
            acc1.withdrow()
        case 2:
            acc1.deposit()
        case 3:
            acc1.checkBalance()
        case 4:
            print("Thank You")
            break
        case _:
            print("Invalid Choice")
