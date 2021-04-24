import datetime, random
now = datetime.datetime.now()

database = {}

def init():
    print("Prime Bank ATM\nWelcome, Dear Customer")
    haveAccountOrNot()

def haveAccountOrNot():
    selected_option = input("Do you have an account with us? \nIf yes, press 1 to login or press 2 to register\n")
    try:
        if int(selected_option) == 1:
            login(database)
        elif int(selected_option) == 2:
            register()
        else:
            print("You have selected an invalid option")
            haveAccountOrNot()
    except ValueError:
        print("You have selected an invalid option")
        haveAccountOrNot()

def login(database):
    inputed_account_number = input("Enter your Account Number: \n")
    is_valid_account_number = account_number_validation(inputed_account_number)

    if is_valid_account_number:
        inputed_password = input("Enter your password: \n")
        is_account_details_valid = account_details_validation(database, inputed_account_number, inputed_password)

        if is_account_details_valid:
            bankOperations(int(inputed_account_number))
        else:
            print("Invalid account number or password")
            haveAccountOrNot()
    else:
        init()

def account_number_validation(inputed_account_number):
    if inputed_account_number:

        if len(str(inputed_account_number)) == 10:
            try:
                int(inputed_account_number)
                return True
            except ValueError:
                print("Invalid Account Number, Account Number should be an integer")
                return False
        else:
            print("Account Number should be ten digits")
            return False

    else:
        print("Account number is a required field")
        return False

def account_details_validation(database, inputed_account_number, inputed_password):
    for account_number in database.keys():
        if int(inputed_account_number) == account_number:
            if inputed_password == database[account_number][-1]:
                return True
        else:
            return False

def bankOperations(account_number):
    print(now.strftime("%Y-%m-%d %H-%M-%S"))
    print(f"Welcome {database[account_number][0]} {database[account_number][1]}")
    print("Press a number to perform the corresponding operation")
    selected_option = input("(1) Withdrawal \n(2) Deposit \n(3) Check Balance \n(4) Complaint \n(5) Exit \n")
    try:
        if int(selected_option) == 1:
            withdraw(account_number)
        elif int(selected_option) == 2:
            deposit(account_number)
        elif int(selected_option) == 3:
            checkBalance(account_number)
        elif int(selected_option) == 4:
            complaint(account_number)
        elif int(selected_option) == 5:
            exit()
        else:
            print("Invalid input")
            bankOperations(account_number)
    except ValueError:
        print("Invalid input")
        bankOperations(account_number)

def withdraw(account_number):
    try:
        amount = int(input("How much do you want to withdraw? \n"))

        if amount <= database[account_number][3]:
            database[account_number][3] -= amount
            print("**********")
            print("******Take your money*****")
            anotherOperation()
        else:
            print("Insufficient Balance")
            anotherOperation()

    except ValueError:
        print("Enter a valid amount")
        withdraw(account_number)

def deposit(account_number):
    try:
        amount = int(input("How much do you want to deposit?: \n"))
        database[account_number][3] += amount
        print("You have just deposited %d naira. Your new account balance is %d naira. " % (amount, database[account_number][3]))
        anotherOperation()

    except ValueError:
        print("Enter a valid amount")
        deposit(account_number)

def checkBalance(account_number):
    print("Your account balance is %d naira" % database[account_number][3])
    anotherOperation()

def complaint(account_number):
    print(f"Further instructions on how to forward your complaints will be sent to your email, {database[account_number][2]}. ")
    print("Thank you for your continued patronage")
    anotherOperation()

def anotherOperation():
    selected_option = input("Do you want to perform another operation?: \n(1) Yes \n(2) No \n")
    try:
        if int(selected_option) == 1:
            login(database)
        elif int(selected_option) == 2:
            exit()
    except ValueError:
        print("Invalid option")
        anotherOperation()


def register():
    print("****** REGISTRATION ******")
    first_name = input("Enter your first name: \n")
    last_name = input("Enter your last name: \n")
    email = input("Enter your email address: \n")
    password = input("Enter your preferred password: \n")
    account_balance = 0

    try:
        account_number = generateAccountNumber()

        database[account_number] = [first_name, last_name, email, account_balance, password]
        print("You have successfully created an account")
        print(f"Your account number is {account_number}\nMake sure to keep it safe")
        loginOrExit()

    except ValueError:
        print("Account Number cannot be generated due to an error...Try again later")
        init()



def loginOrExit():
    selected_option = input("Press 1 to login or press 2 to exit \n")
    try:
        if int(selected_option) == 1:
            login(database)
        elif int(selected_option) == 2:
            exit()
        else:
            print("Please, enter a valid option")
            loginOrExit()
    except ValueError:
        print("Please, enter a valid option")
        loginOrExit()



def exit():
    print("Thank you for using this ATM, Goodbye!")






def generateAccountNumber():
    return int(random.randint(1111111111, 9999999999))


init()