import random

database = {
    1234567890: ["Abioye", "Abdullahi", "walebioye@gmail.com", "password", 1000]
}


def init():
    # Using while loop in a function
    valid_option = False
    print("Welcome to Halal-Bank")
    while valid_option == False:
        have_acct = int(input("Do you have an account with us? \n" "1. Yes \n" "2. No \n"))
        if have_acct == 1:
            valid_option = True
            login()
        elif have_acct == 2:
            valid_option = True
            register()

        else:
            print("Invalid Option Selected")


def login():
    # Using for loop in a function
    print("*********** Enter your Login Details ***********")
    user_acct_no = input("Enter your Account number:")
    valid_acct = account_validation(user_acct_no)
    if valid_acct:
        user_password = input("Enter your password:")
        for acct_number, user_details in database.items():
            if acct_number == int(user_acct_no):
                if user_details[3] == user_password:
                    bank_operation(user_details)

        print('Invalid Account or password')
        login()
    else:
        init()


def register():
    print("********** Register **********")
    email = input("Enter your Email address \n")
    first_name = input("Enter your first name \n")
    last_name = input("Enter your last name \n")
    password = input("Create a password \n")
    account_number = acct_generator()
    database[account_number] = [first_name, last_name, email, password, 0]
    print(f"Your account has been successfully created and your account number is: {acct_generator()}")
    print(f"Thank for for registering with Halal-Bank Mr {first_name} {last_name}")
    print("======== proceed to login ========")
    login()
    try:
        account_number = acct_generator()
    except ValueError:
        print("Account generation failed due to internet connection")
        init()


def bank_operation(user_details):
    print("Welcome %s %s " % (user_details[0], user_details[1]))
    select_an_option = int(input(
        "What would you like to do? \n" "1. Deposit \n" "2. Withdraw \n" "3. Logout \n" "4. Exit \n" "5. balance \n"))
    if select_an_option == 1:
        deposit()
    elif select_an_option == 2:
        withdraw()
    elif select_an_option == 3:
        logout()
    elif select_an_option == 4:
        exit()
    elif select_an_option == 5:
        current_balance(user_details)
    else:
        print("Invalid option selected please try again!")
        bank_operation(user_details)


def deposit():
    print("farabale you go still deposit, make i sharpen my knowledge first")
    init()


def withdraw():
    print("farabale you go still deposit, make i sharpen my knowledge first")
    bank_operation()


def logout():
    print("********** Logout Successful **********")
    login()


def exit():
    init()


def account_validation(account_Number):
    if account_Number:
        if len(str(account_Number)):
            try:
                int(account_Number)
                return True
            except ValueError:
                print("Invalid account number, Account number should be integer")
                return False
            except TypeError:
                print("Invalid account Type")
        else:
            print("Account number can not be less or more than 10")

    else:
        print("Account number is a required field")
        return False


def current_balance(user_details):
    print("Your current balance is \n")
    print(user_details[4])
    bank_operation(user_details)




def acct_generator():
    print("======================================")
    return random.randrange(1111111111, 9999999999)


init()
