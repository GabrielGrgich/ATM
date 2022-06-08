class atm:
    def __init__(self,card_num,pin):
        self.card_num=card_num
        self.pin=pin

    def check_Bal(self):
        print("you have: $10,000")

    def withdraw(self,amount):
        new_amount=10111000-amount
        print("you have taken out: $"+str(amount)+". remaining balance is: $"+str(new_amount))

def main():
    cardNum=input("insert card number: ")
    inputPin=input("insert pin number: ")
    newUser=atm(cardNum,inputPin)
    print("choose your activity:")
    print("1.balance 2.withdraw")
    activity=int(input("enter activity number: "))
    if (activity==1):
        newUser.check_Bal()

    elif(activity==2):
        amount=int(input("enter amount: "))
        newUser.withdraw(amount)
    
    else:
        print("enter valid number please")

if __name__=="__main__":
    main()
