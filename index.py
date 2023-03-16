# design
from colorama import Fore,init
init(autoreset=True)

# # custom package
from BankingSystem.file_handling import FileHandling
from BankingSystem.client import Client
from BankingSystem.database_handling import DatabaseHandling
from BankingSystem import banner

#built in module
import os
import time
import getpass
import sys

#
from rich.progress import Progress
from playsound import playsound


class App:
    def run():
        while True:
            os.system("cls")
            
            print(Fore.GREEN + banner.mainBanner())
            print(Fore.RED+"[1] "+Fore.WHITE+"Login")
            print(Fore.RED+"[2] "+Fore.WHITE+"Create Account\n\n")

            try:
                first_menu = int(input(Fore.WHITE + "Enter Number : "))
            except ValueError:
                os.system("cls")
                print("\n")
                print(Fore.RED + " Only number can accept this input. See the menu for the referrence ".center(100, "*"))
                time.sleep(3)
            else:
                if first_menu >= 1 and first_menu <= 2:
                    if first_menu == 1:
                        os.system("cls")
                        print(Fore.GREEN + banner.mainBanner())
                        user_account_number = input(Fore.WHITE + "Enter your Account Number : ")
                        user_password = getpass.getpass(Fore.WHITE + "Enter your Password : ")

                        file_check = FileHandling(user_account_number, user_password)

                        if file_check.IfClientExist() == 1:
                            playsound("sound/success.mp3")
                            client_handling = DatabaseHandling(account_number = file_check.client_info[0], savings = int(file_check.client_info[1]), firstname = file_check.client_info[2], middlename = file_check.client_info[3], lastname = file_check.client_info[4], password = file_check.client_info[5])
                            while True:
                                os.system("cls")
                                print(Fore.GREEN + banner.mainBanner())
                                print(Fore.RED+"[1] "+Fore.WHITE+"Deposit")
                                print(Fore.RED+"[2] "+Fore.WHITE+"Withdraw")
                                print(Fore.RED+"[3] "+Fore.WHITE+"Profile")
                                print(Fore.RED+"[4] "+Fore.WHITE+"Change Password")
                                print(Fore.RED+"[5] "+Fore.WHITE+"Delete Account\n\n")
                                
                                try:
                                    second_menu = int(input(Fore.GREEN + "Enter Number : "))
                                except ValueError:
                                    os.system("cls")
                                    print("\n")
                                    print(Fore.RED + " Only number can accept this input. See the menu for the referrence ".center(100, "*"))
                                    time.sleep(3)
                                else:
                                    if second_menu >= 1 and second_menu <= 6:
                                        if second_menu == 1:
                                            try:
                                                os.system("cls")
                                                print(Fore.GREEN + banner.depositBanner())
                                                value = int(input("Enter Amount you want to deposit  ₱: "))
                                            except ValueError:
                                                os.system("cls")
                                                print("\n")
                                                print(Fore.RED + " Enter the amount you want to deposit ".center(100, "*"))
                                                time.sleep(3)
                                            else:
                                                client_handling.depositClient(value)
                                                client_handling.fileCommit()
                                                with Progress() as progress:
                                                    task3 = progress.add_task("[green]Loading...", total=100)

                                                    while not progress.finished:
                                                        progress.update(task3, advance=0.5)
                                                        time.sleep(0.02)
                                                        
                                                playsound("sound/atm.mp3")
                                                time.sleep(3)
                                        elif second_menu == 2:
                                            try:
                                                os.system("cls")
                                                print(Fore.GREEN + banner.withdrawBanner())
                                                value = int(input("Enter Amount you want to Withdraw  ₱: "))
                                            except ValueError:
                                                os.system("cls")
                                                print("\n")
                                                print(Fore.RED + " Enter the amount you want to Withdraw ".center(100, "*"))
                                                time.sleep(3)
                                            else:
                                                if(client_handling.savings - value >= 0):
                                                    client_handling.withdrawClient(value)
                                                    client_handling.fileCommit()
                                                    with Progress() as progress:
                                                        task3 = progress.add_task("[green]Loading...", total=100)

                                                        while not progress.finished:
                                                            progress.update(task3, advance=0.5)
                                                            time.sleep(0.02)
                                                    playsound("sound/atm.mp3")
                                                    time.sleep(3)
                                                else:
                                                    os.system("cls")
                                                    print("\n")
                                                    print(Fore.RED + f" Can't withdraw because your current savings is ₱ {client_handling.savings}  ".center(100, "*"))
                                                    time.sleep(3)
                                        elif second_menu == 3:
                                            os.system("cls")
                                            print(Fore.GREEN + banner.profileBanner())
                                            print(client_handling.displayClientInfo())
                                            input(Fore.BLUE + "Press enter to continue ... ")
                                            time.sleep(3)
                                        elif second_menu == 4:
                                            try:
                                                os.system("cls")
                                                print(Fore.GREEN + banner.changePasswordBanner())
                                                new_password = input("Enter new Password : ")
                                            except ValueError:
                                                os.system("cls")
                                                print("\n")
                                                print(Fore.RED + " Pls use a valid password ".center(100, "*"))
                                                time.sleep(3)
                                            else:
                                                client_handling.updatePassword(new_password)
                                                client_handling.fileCommit()
                                                with Progress() as progress:
                                                    task3 = progress.add_task("[green]Updating...", total=100)

                                                    while not progress.finished:
                                                        progress.update(task3, advance=0.5)
                                                        time.sleep(0.02)
                                                time.sleep(3)
                                        elif second_menu == 5:
                                            os.system("cls")
                                            print(Fore.GREEN + banner.deletePasswordBanner())
                                            client_handling.deleteClient()
                                            with Progress() as progress:
                                                task3 = progress.add_task("[red]Deleting...", total=100)

                                                while not progress.finished:
                                                    progress.update(task3, advance=0.5)
                                                    time.sleep(0.02)
                                            time.sleep(3)
                                            break
                                    else:
                                        os.system("cls")
                                        print("\n")
                                        print(Fore.RED + " Invalid input ".center(100, "*"))
                                        time.sleep(3)
                        else:
                            os.system("cls")
                            print("\n")
                            print(Fore.RED + " You don't have an account. Pls create one before login ".center(100, "*"))
                            playsound("sound/loginFailed.mp3")
                            time.sleep(3)
                    elif first_menu == 2:
                        os.system("cls")
                        print(Fore.GREEN + banner.createAcc())

                        user_fname = input("Enter your Firstname : ")
                        user_mname = input("Enter your Middlename : ")
                        user_lname = input("Enter your Lastname : ")
                        user_password = input("Enter your Password : ")

                        client = DatabaseHandling(account_number = None, savings = None, firstname = user_fname, middlename = user_mname, lastname = user_lname, password = user_password)
                        client.setAccountNumber()
                        client.setSavings()
                        client.createClient()

                        playsound("sound/success.mp3")
                        print(Fore.GREEN + "\n Sign Up Successfully !")
                        time.sleep(3)

                        os.system("cls")
                        print(Fore.GREEN + banner.profileBanner())
                        print(client.displayClientInfo())

                        print(Fore.GREEN + " Note: remember your account number and password")
                        input(Fore.BLUE + " Press enter to continue ... ")
                        time.sleep(3)
                else:
                    os.system("cls")
                    print("\n")
                    print(Fore.RED + " Only 1 and 2 number will be accepted ".center(100, "*"))
                    time.sleep(3)
    
    def __repr__(self):
        return """
Banking System

The users can update their accounts, where they can deposit and withdraw their savings. It is also capable of opening 
another account and deleting it. At the same time, it also has a database that stores its information. 
This banking system's primary function is Create-Read-Update-Delete.

"""

if __name__ == "__main__":
    if len(sys.argv) == 1:
        App.run()
    else:
        if sys.argv[1] in ["--help", "-h"]:
            print(repr(App()))
    
    
