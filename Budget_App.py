class budget:
    """
    This is a Budget App
    """
    def food(self):
        print("Welcome to Food Budget.")
        print("Available Options: \n")
        print("1. deposit")
        print("2. Withdraw")
        print("3. Transfer")

    def clothing(self):
        print("Welcome to Clothing Budget")
        print("Available Options: \n")
        print("1. deposit")
        print("2. withdraw")
        print("3. Transfer")

    def entertaiment(self):
        print("Welcome to Entertainment Budget")
        print("Available Options: \n")
        print("1. deposit")
        print("2. withdraw")
        print("3. Transfer")

    def deposit(self):

        print("Maximum deposit is 1000000")
        Balance = 1000
        deposit = float(input("How much would you like to deposit? \n"))
        print("You deposited %s to your food budget" % deposit)
        availableBalance = int(Balance) + int(deposit)
        print("*****************")
        print("Your Balance is: %s" % availableBalance)

    def withdraw(self):
        print("Minimum you can withdraw is 1000")
        Balance = 1000
        withdraw = float(input("How much would you like to withdraw from your food budget? \n"))
        print("You withdraw %s from your food budget" % withdraw)
        availableBalance = int(Balance) - int(withdraw)
        print("*****************")
        print("Your Balance is: %s" % availableBalance)

    def Transfer(self):
        Transfer = float(input("How much would you like to Transfer from your food budget? \n"))
        print("Maximum you can Transfer is 1000")
        print("You can transfer between your budget category\n")
        print("1. food")
        print("2. clothing")
        print("3. entertainment")
        print("...........................")

        TransferOption = float(input("Where would you like to transfer to? \n"))
        if TransferOption == 1:
            print(Transfer)
            print(f"You successfully transfer {Transfer} to food budget")
            Balance = 1000
            availableBalance = int(Balance) + int(Transfer)
            print("*****************")
            print("Your Balance is: %s" % availableBalance)
        elif TransferOption == 2:
            print(Transfer)
            print(f"You successfully transfer {Transfer} to clothing budget")
            Balance = 1000
            availableBalance = int(Balance) + int(Transfer)
            print("*****************")
            print("Your Balance is: %s" % availableBalance)

        elif TransferOption == 3:
            print(Transfer)
            print(f"You successfully transfer {Transfer} to entertainment budget")
            Balance = 1000
            availableBalance = int(Balance) + int(Transfer)
            print("*****************")
            print("Your Balance is: %s" % availableBalance)
        else:
            print("Invalid option selected")



def main():
    print('select your budget category: \n')
    print("1. food")
    print("2. clothings")
    print("3. entertainment")
    print()
    selectCategory = int(input("Select your budget Category: \n"))
    if selectCategory == 1:
        Budget = budget()
        Budget.food()
        foodOption = int(input("Select an Option:"))
        if foodOption == 1:
            foodDep = budget()
            foodDep.deposit()


        elif foodOption == 2:
            foodWith = budget()
            foodWith.withdraw()


        elif foodOption == 3:
            foodTrans = budget()
            foodTrans.Transfer()




        else:
            print("Invalid option selected! Please try again")

    elif selectCategory == 2:
        Budget = budget()
        Budget.clothing()
        clothOption = int(input("Select an Option:"))
        if clothOption == 1:
            print("Maximum deposit is 1000000")
            Balance = 1000
            deposit = float(input("How much would you like to deposit? \n"))
            print("You deposited %s to your Clothing budget" % deposit)
            availableBalance = int(Balance) + int(deposit)
            print("*****************")
            print("Your Balance is: %s" % availableBalance)

        elif clothOption == 2:
            print("Minimum you can withdraw is 1000")
            withdraw = float(input("How much would you like to withdraw from your Clothing budget? \n"))
            Balance = 1000
            print("You withdraw %s from your clothing budget" % withdraw)
            availableBalance = int(Balance) - int(withdraw)
            print("*****************")
            print("Your Balance is: %s" %availableBalance)

        elif clothOption == 3:
            Transfer = float(input("How much would you like to Transfer from your clothing budget? \n"))
            print("Maximum you can Transfer is 1000")
            print("You can transfer between your budget category\n")
            print("1. food")
            print("2. clothing")
            print("3. entertainment")
            print("...........................")

            TransferOption = float(input("Where would you like to transfer to? \n"))
            if TransferOption == 1:
                print(Transfer)
                print(f"You successfully transfer {Transfer} to food budget")
                Balance = 1000
                availableBalance = int(Balance) + int(Transfer)
                print("*****************")
                print("Your Balance is: %s" % availableBalance)
            elif TransferOption == 2:
                print(Transfer)
                print(f"You successfully transfer {Transfer} to clothing budget")
                Balance = 1000
                availableBalance = int(Balance) + int(Transfer)
                print("*****************")
                print("Your Balance is: %s" % availableBalance)

            elif TransferOption == 3:
                print(Transfer)
                print(f"You successfully transfer {Transfer} to entertainment budget")
                Balance = 1000
                availableBalance = int(Balance) + int(Transfer)
                print("*****************")
                print("Your Balance is: %s" % availableBalance)

            else:
                print("Invalid option selected")

        else:
            print("Invalid option selected! Please try again")

    elif selectCategory == 3:
        Budget = budget()
        Budget.entertaiment()
        Option = int(input("Select an Option:"))
        if Option == 1:
            print("Maximum deposit is 1000000")
            Balance = 1000
            deposit = float(input("How much would you like to deposit? \n"))
            print("You deposited %s to your Entertainment budget" % deposit)
            availableBalance = int(Balance) + int(deposit)
            print("*****************")
            print("Your Balance is: %s" % availableBalance)

        elif Option == 2:
            print("Minimum you can withdraw is 1000")
            Balance = 1000
            withdraw = float(input("How much would you like to withdraw from your Entertainment budget? \n"))
            print("You withdraw %s from your Entertainment budget" % withdraw)
            availableBalance = int(Balance) - int(withdraw)
            print("*****************")
            print("Your Balance is: %s" % availableBalance)

        elif Option == 3:
            Transfer = float(input("How much would you like to Transfer from your Entertainment budget? \n"))
            print("Maximum you can Transfer is 1000")
            print("You can transfer between your budget category\n")
            print("1. food")
            print("2. clothing")
            print("3. entertainment")
            print("...........................")

            TransferOption = float(input("Where would you like to transfer to? \n"))
            if TransferOption == 1:
                print(Transfer)
                print(f"You successfully transfer {Transfer} to food budget")
                Balance = 1000
                availableBalance = int(Balance) + int(Transfer)
                print("*****************")
                print("Your Balance is: %s" % availableBalance)
            elif TransferOption == 2:
                print(Transfer)
                print(f"You successfully transfer {Transfer} to clothing budget")
                Balance = 1000
                availableBalance = int(Balance) + int(Transfer)
                print("*****************")
                print("Your Balance is: %s" % availableBalance)

            elif TransferOption == 3:
                print(Transfer)
                print(f"You successfully transfer {Transfer} to entertainment budget")
                Balance = 1000
                availableBalance = int(Balance) + int(Transfer)
                print("*****************")
                print("Your Balance is: %s" % availableBalance)

            else:
                print("Invalid option selected")

        else:
            print("Invalid option selected! Please try again")

    else:
        print("Invalid Option selected! Try again")

if __name__ == '__main__':
    main()

