""" CFG WEEK 4 HOMEWORK
Author: Daniella Omokore

(Exception Handling)

Simple ATM program
Using exception handling code blocks such as try/ except / else / finally, write a program that simulates an ATM machine to withdraw money.
(NB: the more code blocks the better, but try to use at least two key words e.g. try/except)
Tasks:
1.       Prompt user for a pin code
2.       If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again. You can give a user a maximum of 3 attempts and then exit a program.
3.       Set account balance to 100.
4.       Now we need to simulate cash withdrawal
5.       Accept the withdrawal amount
6.       Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be negative!)
7.       However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an error an exit the program.


"""


correctPin = 1234 #Initialise a correct pin code

attempts = 0  #Initialise count of attemps to zero

""" I created my own user defined exception  """
class negativeBalanceError(ValueError):
    #Raised when the balance is a negative number
    pass



""" Allows the user to withdraw money """
def withdrawMoney():
    accountBalance = 100
    try:
        withdrawAmount = int(input("Enter withdraw amount: £"))
        accountBalance = accountBalance - withdrawAmount
        if accountBalance < 0:
            raise negativeBalanceError

    except negativeBalanceError:
        print("You can't withdraw more than your available balance, Please Enter a valid amount.")

    else:
        print("Your withdraw of £" + str(withdrawAmount) +  " has been Successfull. Your remaining balance is £" + str(accountBalance)+".")

    finally:
        print("Transaction Complete, Thanks for Using this ATM.")


""" Checks if the users Pin is correct to grant access """
while attempts < 3:
    pin = int(input("Please enter your pin:"))
    if pin == correctPin:
        print("Access granted")
        withdrawMoney()
        break
    elif attempts < 3:
        print("Incorrect pin, Try again")
        attempts += 1







