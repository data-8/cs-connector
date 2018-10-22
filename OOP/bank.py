from account import CheckingAccount, SavingsAccount

class Bank:   
    _accounts = []
    
    def add_account(self, name, account_type, initial_deposit):
        if account_type == 'Savings':
            new_account = SavingsAccount(name, initial_deposit)
        elif account_type ==  'Checking':
            new_account = CheckingAccount(name, initial_deposit)
        else:
            assert True, "Bad Account type: " + account_type
        assert initial_deposit > 0, "Bad deposit"
        
        Bank._accounts.append(new_account)
        return new_account
    
    def accounts(self):
        return self._accounts[:]

    def show_accounts(self):            
        for acct in self.accounts():
            print(acct.account_number(), acct.account_type(), 
                  acct.account_name(), acct.account_balance())
            
    def total_assets(self):
        return sum([acct.account_balance() for acct in self.accounts()])


# A little application example
def main():
    bank = Bank()
    spock_acct = bank.add_account('Spock', 'Savings', 1010)
    kirk_acct = bank.add_account('Captain Kirk', 'Checking', 2020)
    scotty_acct = bank.add_account('Engineer Scott', 'Savings', 111111)
    
    bank.show_accounts()
    print(bank.total_assets())

if __name__ == "__main__":
    # execute only if run as a script
    main()

    
