# Log in system right here

# Importing all functions
import time

# Defining all functions


def Homepage():
    # Start up page
    print("Welcome to the home screen of redox, please enter the system")

    # Login or sign up
    Option = input(
        "Chose one of the following options\n1:\tLog in to existing account\n2:\tSign up for a new account\n3:\tExit Window\n[Input Option]\t")
    while Option != "1" and Option != "2" and Option != "3":
        print("Not a valid response.")
        Option = input(
            "Chose one of the following options\n1:\tLog in to existing account\n2:\tSign up for a new account\n3:\tExit Window\n[Input Option]\t")

    if Option == "1":
        LogIn()
    elif Option == "2":
        SignUp()
    else:
        input("input enter to exit")
    return Option


def LogIn():
    # Load LogIn
    print("loading")
    time.sleep(1)
    print("...")
    print("loading")
    time.sleep(1)
    print("Welcome to the log in page")

    # Variables that will be used soon
    valid_name = False
    valid_password = False
    Count = 0

    UserInp = input("Input your username.\t")
    for n in range(0, len(Users)):
        if UserInp == Users[n]:
            valid_name = True
            x = n
        else:
            pass

    if valid_name:
        # Inputting password if username is valid only
        while Count < 3:
            PasswordInp = input("Input your password.\t")
            if PasswordInp == Passwords[x]:
                valid_password is True
                print("You have logged in successfully")
                Count = 3
            else:
                print("Wrong password")
                Count += 1

        if valid_password:
            Sign_in = True

        else:
            Sign_in = False
            print("Redirecting to home page")
            Homepage()

    else:
        Sign_in = False
        print("Redirecting to home page")
        Homepage()
    return Sign_in


def SignUp():
    # Load SignUp page
    print("loading")
    time.sleep(1)
    print("...")
    print("loading")
    time.sleep(1)
    print("Welcome to the sign up page")

    UserInp = input("Input your username:\t")
    for n in range(0, len(Users)):
        if UserInp == Users[n]:
            print("Username already taken, redirecting back to the sign in page...")
            SignUp()
        else:
            break

    PasswordInp = input("Please enter a password:\t")
    PasswordInp2 = input("Please confirm your password:\t")

    if PasswordInp != PasswordInp2:
        print("Passwords don't match, redirecting to Sign up page...")
        SignUp()
    elif len(PasswordInp) < 8:
        print("Password is too short, password needs to be atleast 8 characters. Reloading page")
        SignUp()
    else:
        Users.append(UserInp)
        Passwords.append(PasswordInp)


# Defining all variables and CONSTANTS
Option = "1"

# Declaring lists
Users = ["leeN"]
Passwords = ["leeN"]

# Program start
while Option != "3":
    Option = Homepage()
