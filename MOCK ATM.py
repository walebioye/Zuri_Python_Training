#name = input("what is your name? \n")
#allowedUsers = ['seyi', 'mike', 'Abioye']
#allowedPassword = "Passkey"
#if(name in allowedUsers):
 #   password = input("Enter your password \n")
  #  if(password == allowedPassword):
   #     print("Welcome %s " % name)
   # else:
    #    print('passsword incorrect, please try again')
#else:
 #   print('name not found, please try again')
# name = input("what is your name? \n")
# allowedusers = ('citcc', 'ipnx', 'ihs')
# allowedpassword = ('passcitcc', 'passipnx', 'passihs')
# if(name in allowedusers):
#     password = input("enter your password \n" )
#     userid = allowedusers.index(name)
#     if(password == allowedpassword[userid]):
#         print('welcome to %s' % name)
#         print('these are the available options:')
#         print('1. withdrawer')
#         print('2. cash deposit')
#         print('3. complaint')

#         selectedoption = int(input('please select an option'))

#         if(selectedoption == 1):
#             print("you  selected %s" % selectedoption)
#         elif(selectedoption == 2):
#             print("you selected %s" % selectedoption)
#         elif(selectedoption == 3):
#             print("you selected %s" %selectedoption)
#         else:
#             print("invalid option selected, pleae try again ")

#     else:
#         print("pasword incorrect, please try again")

# else:
#     print('name not found, please try again')





#ASSIGNMENT
import datetime
# import sys
now = datetime.datetime.now()
#print("current date and time  : ")S
# print(now.strftime("%y-%m-%d %h:%m:%s"))
name = input("What is your name? \n")
allowedUsers = ('Abioye', 'Abdullahi', 'Adewale')
allowedPassword = ('passwordAbioye', 'passwordAbdullahi', 'passwordAdewale')
availableBalance = [1125000, 125000, 5000000]
accountLimit = [100000000, 100000000, 100000000]
allowedDeposit = [5000, 10000, 20000]
complaintsOutput = ("Thank you for contacting us")

if(name in allowedUsers):
    password = input("Please Enter Your Password \n")

    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print("WELCOME Mr %s" %name.upper())
        print("You are now looged in : %s" %now)
        print("These are the available options: \n")
        print('1. Withdrawal')
        print('2. Cashdeposit')
        print('3. Complaints')

        selectOption = int(input('Please select an option: \n'))
        
        #forWithdrawal
        if(selectOption == 1):
            print("You selected %s" %selectOption)
            withdrawal = float(input('How much would you like to withdraw? \n'))
            withdrawalAmount = [1000, 5000, 10000]
           
            if(withdrawal <= availableBalance[userId]):
                print('withdrawal : %s' %withdrawal)
                print('please take your cash \n')
                 
            else:
                print("Transaction Declined.... Insufficient balance.....")
            
        #Deposit
        elif(selectOption == 2):
            print("You selected %s" %selectOption)
            deposit = float(input("How much would you like to deposit? \n"))
            if(deposit <= accountLimit[userId]):
                print('Your Deposit : %s' %deposit)
                currentBalance = int(deposit) + availableBalance[userId]
               
                if(deposit >= allowedDeposit[userId]):
                    print('Current Balance: %s' %currentBalance)
                    
                                       
            else:
                print("Maxixmum Amount Exceeded")
                
        #Complaint
        elif(selectOption == 3):
            print("You selected %s" %selectOption)
            complaints = input("What issue will you like to report? \n")
            print("Issue to be Address : %s \n" %complaints)
            print(complaintsOutput)

        else:
            print('Invalid Option Selected, Please try again')
            
    else:
        print('Password incorrect, please try again')
else:
    print("Name not found, Try again")

            
       

        

           