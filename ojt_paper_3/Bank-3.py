class Bank():
    def __init__(self):
        self.Amount=0 

    def credit(self,credit_amount):
        self.Amount=self.Amount+credit_amount 
    
    def debit(self,debit_amount):
        if debit_amount < self.Amount:
            print("Insufficent balance to withdraw amount")
        self.Amount=self.Amount-debit_amount 

        


    
