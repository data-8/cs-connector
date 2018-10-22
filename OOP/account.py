class Account:
    """Create named accounts with a balance that is 
    - increased by account_deposit
    - decreased by account_withdrawl
    """
        
    # Class astributes outside and class defs
    _account_number_seed = 1000
    
    # Constructor
    
    def __init__(self, name, initial_deposit): 
        # Initialize the instance attributes
        self._name = name 
        self._acct_no = Account._account_number_seed     
        Account._account_number_seed += 1
        self._balance = initial_deposit
        # Return None
        
    # Selectors
    
    def account_name(self):
        return self._name

    def account_balance(self):
        return self._balance
    
    def account_number(self):
        return self._acct_no
    
    # Operations
    
    def deposit(self, amount):
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        self._balance -= amount
        return self._balance
    
    # Display representation
    def __repr__(self):
        return '<Account: ' + str(self.account_name()) + '-' + str(self.account_number()) + '>'
    # Print representation
    def __str__(self):
        return '<Account: ' + str(self.account_name()) + '-' + str(self.account_number()) + '>'

class CheckingAccount(Account):
    
    def __init__(self, name, initial_deposit):
        # Use superclass initializer
        Account.__init__(self, name, initial_deposit)
        # Additional initialization
        self._type = "Checking"
    
    def account_type(self):
        return self._type
    
    # Display representation
    def __repr__(self):
        return '<' + str(self.account_type()) + 'Account: ' + str(self.account_name()) + '-' + str(self.account_number()) + '>'
    # Print representation
    def __str__(self):
        return '<' + str(self.account_type()) + 'Account: ' + str(self.account_name()) + '-' + str(self.account_number()) + '>'


class SavingsAccount(Account):
    
    interest_rate = 0.02
    
    def __init__(self, name, initial_deposit):
        # Use superclass initializer
        Account.__init__(self, name, initial_deposit)
        # Additional initialization
        self._type = "Savings"
    
    def account_type(self):
        return self._type
    
    def acrue_interest(self):
        self._balance = self._balance * (1 + SavingsAccount.interest_rate)
    
    # Display representation
    def __repr__(self):
        return '<' + str(self.account_type()) + 'Account: ' + str(self.account_name()) + '-' + str(self.account_number()) + '>'
    # Print representation
    def __str__(self):
        return '<' + str(self.account_type()) + 'Account: ' + str(self.account_name()) + '-' + str(self.account_number()) + '>'

