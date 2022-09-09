#THIS CODE IS REFACTORED FOR THE UNIT TESTS-NOT ANS TO Q2#


correctPin = 1234 #Initialise a correct pin code

def accountAccess(pin):
    attempts = 0  #Initialise count of attemps to zero
    while attempts < 3:
        if pin == correctPin:
           #withdrawMoney()
            print("Access granted")
            return True
        elif attempts < 3:
            attempts += 1
            print("Incorrect pin, Try again")
            return False



""" I created my own user defined exception  """
class negativeBalanceError(ValueError):
    #Raised when the balance is a negative number
    pass



""" Allows the user to withdraw money """
def withdrawMoney(withdrawAmount):
    accountBalance = 100
    try:
        accountBalance = accountBalance - withdrawAmount
        if accountBalance < 0:
           #raise negativeBalanceError
            return False
    except negativeBalanceError:
        print("You can't withdraw more than your available balance, Please Enter a valid amount.")

    else:
        print("Your withdraw of £" + str(withdrawAmount) +  " has been Successful. Your remaining balance is £" + str(accountBalance)+".")
        return True

    finally:
        print("Transaction Complete, Thanks for Using this ATM.")







