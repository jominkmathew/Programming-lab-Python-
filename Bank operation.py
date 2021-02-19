class account:
    def __init__(self):
        self.bal=0
        self.name=input("Enter the name:")
        self.type=input("Enter the account type")
    def display(self):
        print("name:",self.name)
        print("Account Type:",self.type)
    def deposit(self):
        amount=int(input("Enter the ammount to deposit"))
        self.bal+=amount
        print("Account Balanace:",self.bal)
    def withdraw(self):
        if self.bal==0:
            print("Insfficient Balance")
        else:
            amount=int(input("Enter the ammount to withdraw"))
            current=self.bal
            self.bal-=amount
            if self.bal < 0:  
                self.bal=current
                print("Insufficient Balance")
            else:       
                print("Account Balanace:",self.bal)
            
        

ac1=account()
ac1.display()
ac1.deposit()
ac1.withdraw()
