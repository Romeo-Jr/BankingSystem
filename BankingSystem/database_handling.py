# # custom package
from BankingSystem.client import Client

#built in module
import os

class DatabaseHandling(Client):
    def __init__(self, **client_info):
        super().__init__(**client_info)


    def fileCommit(self):
        temp_file = open("temp_file.txt",mode="w")
        file = open("database.txt", "r")

        for line in file:
            toList = line.split("/")
            if(toList[0] == self.account_number):
                temp_file.write(f"{self.account_number}/{self.savings}/{self.firstname}/{self.middlename}/{self.lastname}/{self.password}\n")
            else:
                temp_file.write(f"{ toList[0] }/{ toList[1] }/{ toList[2] }/{ toList[3] }/{ toList[4] }/{ toList[5] }")

        temp_file.close()
        file.close()

        os.remove("database.txt")
        os.rename("temp_file.txt","database.txt")
    
    def createClient(self):
        with open("database.txt", "a") as data:
            data.write(f"{self.account_number}/{self.savings}/{self.firstname}/{self.middlename}/{self.lastname}/{self.password}\n")