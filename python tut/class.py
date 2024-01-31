class Atm:
    #constructor in python class
    def __init__(self):
     self.pin=""
     self.balance = 0
     self.menu()

    def menu(self):
       userinput=input('''
                
            how would you like to proceed?
            1. Enter 1 to create PIN
            2. Enter 2 to Deposit
            3. Enter 3 to withdraw
            4. Enter 4 to cheack balance
            5. Enter 5 to exit
       ''')
       if userinput == '1':
          self.create_pin()


       elif userinput == '2':
          self.deposit()

       elif userinput == '3':
          self.withdraw_amount()

       elif userinput == '4':
          self.check_balance()
       else:
          print('bye')

#to define a methord for pin creation
    def create_pin(self):
          pin=input('enter your pin :\n')
          self.pin=pin
          print('PIN SET!')
        
# methord for Deposit amount
    def deposit(self):
          temp=input('enter your PIN :\n')
          
          ''' #if the PIN is not created yet
          if self.pin == "":
            print("Please create a PIN first.")
            return'''
          if temp == self.pin:
             amount=int(input('how much amount you want to deposit'))
             self.balance = self.balance + amount
             print('amount has been deposit successfuly!')
          else:
             print("invalid Pin")

# methord for Withdraw_amount
    def withdraw_amount(self):
        temp=input('enter your PIN :\n')
          
        if temp == self.pin:
             amount=int(input('how much amount you want to withdraw'))
             if amount<=self.balance:
                self.balance = self.balance - amount
                print('operation successful')
             else:
                print("insufficent fund")
        
        else:
            print('invalid PIN')

# methord for checking balance
    
    def check_balance(self):
        temp=input('enter your PIN :\n')
          
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalide pin")

#to create an object of a class 

while True:
 A1=Atm()
 A1.deposit()
 A1.withdraw_amount()
 A1.check_balance()

 #let we create anther object (instance of the class for anther user)
 A2=Atm()
 A2.deposit()
 A2.withdraw_amount()

 #Similarly we can create further objects for many users 
 #so this is the speciality of an object which keep each recode separte 
 ch=input("do you want to go to main menu (y/n) ")
 if ch.lower() != 'y':
    break


