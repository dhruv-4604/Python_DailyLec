class ATM:
    def createPin(self):
        status=False
        while(not status):
            temp_pin=int(input("Enter New Pin to Set:"))
            if temp_pin<1000 or temp_pin>9999:
                print("Invalid Pin!\nPin Must be of 4 digit.\n")
                continue;
            confirm_pin=int(input("Enter The Pin Again to Confirm:"))
            if temp_pin!=confirm_pin:
                print("Confirm Pin Not Match!\nTry Again to set.\n")
                continue;
            self.atm_pin=confirm_pin
            status=True
        else:
            self.atm_bal=float(input("Enter Balance: "))
            print("Pin Set Successfully!")
            print(f"Your Account Balance is {self.atm_bal}.\n\n")
            
            
    def changePin(self):
        status=False
        while(not status):
            check_pin=int(input("Enter Your Old Pin:"))
            if check_pin!=self.atm_pin:
                print("Invalid Pin\nTry Again.\n")
                continue
            temp_pin=int(input("Enter Your Pin to Set:"))
            if temp_pin<1000 or temp_pin>9999:
                print("Invalid Pin!\nPin Must be of 4 digit.\n")
                continue;
            confirm_pin=int(input("Enter The Pin Again to Confirm:"))
            if temp_pin!=confirm_pin:
                print("Confirm Pin Not Match!\nTry Again to set.\n")
                continue;
            self.atm_pin=confirm_pin
            status=True
        else:
            print("Pin Set Successfully!")
        
    def checkBalance(self):
        print(f"Your Account Balance is {self.atm_bal}.\n\n")
        
    def withdraw(self):
        amount=float(input("Enter Amount To Withdraw: "))
        if amount>self.atm_bal:
            print("\nInsufficient Balance.")
        else:
            self.atm_bal-=amount
            self.checkBalance()
            

            
            
print("Welcome To XYZ BANK ATM\n\n")
atm=ATM()
atm.createPin()
user_inp=5
while(user_inp!=0):
    user_inp=int(input("\n------------ MENU ------------\n1. Change Pin\n2. Withdraw Amount\n3.Check Balance\n0.Exit\n------------------------------\nEnter Choice:"))
    if user_inp==1:
        atm.changePin()
    elif user_inp==2:
        atm.withdraw()
    elif user_inp==3:
        atm.checkBalance()
    else:
        print("Invalid Choice!")
else:
    print("\n\nThank You for Visiting!")
