import random

class Client:
    def __init__(self, **client_info ):

        self.account_number = client_info["account_number"]
        self.firstname = client_info["firstname"]
        self.middlename = client_info["middlename"]
        self.lastname = client_info["lastname"]
        self.password = client_info["password"]
        self.savings = client_info["savings"]
    
    def setSavings(self):
        self.savings = 0
    
    def setAccountNumber(self):
        client_account__number = f"{random.randint(100000,999999)}-{random.randint(100000,999999)}-{random.randint(100000,999999)}"
        self.account_number = client_account__number

    def depositClient(self, amount):
        self.savings += amount
    
    def withdrawClient(self, amount):
        self.savings -= amount
    
    def updatePassword(self, new_password):
        self.password = new_password
    

    def displayClientInfo(self):
        return f"""
    Account Number : {self.account_number}
    Firstname : {self.firstname}
    Middlename : {self.middlename}
    Surname : {self.lastname}
    Savings : ₱ {self.savings}.00
    Password : {self.password}
 
        """
    
    def deleteClient(self):
        with open("database.txt","r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if self.account_number not in line:
                    f.write(line)
            f.truncate()
    

    
