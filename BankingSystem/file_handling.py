class FileHandling:
    def __init__(self, client_account_number , client_password, client_info = []):
        self.client_account_number = client_account_number
        self.client_password = client_password
        # 0 =  account number
        # 1 =  savings
        # 2 =  first name
        # 3 = middle name
        # 4 = last name
        # 5 = password
        self.client_info = client_info
    

    def IfClientExist(self):
        file = open("database.txt", "r")
        returnVal = 0
        for line in file:
            toList = line.split("/")
            if(toList[0] == self.client_account_number and toList[-1].strip() == self.client_password):
                for idx in range(6):
                    if idx == 5:
                        self.client_info.append(toList[idx].strip())
                    self.client_info.append(toList[idx])

                returnVal += 1

        return returnVal
    
