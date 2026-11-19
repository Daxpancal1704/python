"""### Question 6 (Medium) - Encapsulation
Create a class `BankAccount` with a **private** balance. Add `deposit(amount)`, `withdraw(amount)` and `get_balance()`.
* An amount of `0` or less raises `ValueError("Amount must be positive")`.
* Withdrawing more than the balance raises `ValueError("Insufficient balance")`.
* The balance must **not** be reachable as `acc.__balance` from outside the class.

Make this test code produce the output below:
```python
acc = BankAccount("Asha", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())

for action, amount in [(acc.withdraw, 5000), (acc.deposit, -50)]:
    try:
        action(amount)
    except ValueError as e:
        print("Error:", e)

try:
    print(acc.__balance)
except AttributeError:
    print("Cannot access private balance")
```
```
1300
Error: Insufficient balance
Error: Amount must be positive
Cannot access private balance
```"""


class BankAccount:
    def __init__(self,owner,balance:float=0):
        self.owner=owner
        if balance < 0:
            raise ValueError("Initial Balance is cannot be negative ")
        self.__balance=balance

    def deposite(self,amount:float):
        if amount <= 0:
            raise ValueError("Amount must be positive ")
        self.__balance +=amount


    def withdraw(self,amount:float):
        if amount <= 0:
            raise ValueError ("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficent balance")
        self.__balance -=amount

    def get_balance(self):
        return self.__balance
try:    
    owner=input("Owner name :")
    balance=float((input("Balance :")))
    # acc=BankAccount("Dax",50000)
    acc=BankAccount(owner,balance)
    acc.deposite(10000)
    acc.withdraw(30000)
    print(acc.get_balance())    
except ValueError as e:
    print("error :",e)