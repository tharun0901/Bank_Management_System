from bank import Bank
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s")
class BankManagement:
    @staticmethod
    def main()->None:
     account = None
     while True:
        print("1. Create account")
        print("2. Account details")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. cancel")
        opt = input("select options from the above:").strip()
        if opt == "1":
           name = input("Enter your name:")
           age = input("Enter your age:")
           branch = input("Enter the branch:")
           account_no = input("Enter the accunt number").strip()
           account = Bank(name,age,branch,account_no)
           account.file_write()
           account.database()
           logging.info("Account created successfully")
        elif opt == "2":
           acc_no=input("Enter your account number:").strip()
           account=Bank.fetch_details(acc_no)
           if account:
              detail = account.getter()
              for k,v in detail.items():
                 print(f"{k}:{v}")
           else:
              logging.warning("no account details")
        elif opt == "3":
            acc_no=input("Enter your account number:").strip()
            account=Bank.fetch_details(acc_no)
            if account:
               amount = float(input("Enter amount you want to deposit: "))
               account.deposit(amount)
               account.file_write()
               account.update_balance()
            else:
               logging.warning("no account")

        elif opt == "4":
            acc_no=input("Enter your account number:").strip()
            account=Bank.fetch_details(acc_no)
            if account:
                amount = float(input("Enter amount you want to withdraw: "))
                account.withdraw(amount)
                account.file_write()
                account.update_balance()
            else:
               logging.warning("no account")
        elif opt == "5":
           print("exit")
           break
        else:
           logging.error("Invalid input")

BankManagement.main()
