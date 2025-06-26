import cx_Oracle
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s")
class Bank:
    def __init__(self, name: str, age: int, branch: str, account_no: str, balance: float=0.0):# constructor
        """ variable with private access modifier"""
        self.__name = name       
        self.__age = age        
        self.__branch = branch   
        self.__account_no = account_no       
        self.__balance = float(balance)  
    def getter(self)->dict:     
        """it is a getter method where the all values return in the form of dictionary""" 
        return{
            "name":self.__name,
            "age":self.__age,
            "branch":self.__branch,
            "account_no":self.__account_no,
            "balance":self.__balance
        }
    def deposit(self, amount: float)-> None:
        """Deposite amount"""
        if amount > 0:   # when the client deposit amount more than 0
            self.__balance += amount  # when the deposited here the balance will be updated
            logging.info(f"Deposited amount is :{amount} and now total balnace is:{self.__balance}" )
        else:
            logging.warning("please deposite amount you have low balance")
    def withdraw(self, amount: float)-> None:
        """withdraw amount"""
        if amount <= self.__balance: # when the client withdraw amount less than or equal to balace
            self.__balance -= amount # after the withdraw the remaining balance will be shown
            logging.info(f"withdraw amount is {amount} and your remaining balance is{self.__balance}")
        else:
            logging.error("you have insufficient balance")
    def file_write(self)-> None:
        """writing the account details in the files"""
        file = f"{self.__account_no}.txt"  
        with open(file, "w") as f:     
            f.write(f"{self.__name}\n")  
            f.write(f"{self.__age}\n")   
            f.write(f"{self.__branch}\n")  
            f.write(f"{self.__account_no}\n")
            f.write(f"{self.__balance}\n")   
    @staticmethod
    def file_read(account_no: str)->"Bank":
        """reading the account details"""
        file = f"{account_no}.txt"
        with open(file,"r")as f: 
            name = f.readline().strip() 
            age = f.readline().strip()  
            branch = f.readline().strip() 
            account_no = f.readline().strip() 
            balance= float(f.readline().strip()) 
            return Bank(name, age, branch, account_no, balance) # it is returning the object with the values
    def database(self)-> None:
        """saving the data in oracle database"""
        try:
            dsn = cx_Oracle.makedsn("localhost" ,1521 ,service_name = "orcl")
            con = cx_Oracle.connect(user = "tharun",password = "tharun",dsn=dsn)
            c = con.cursor()
            c.execute(""" insert into bank_management(name,age,branch,account_no,balance) values(:1, :2, :3, :4, :5)""",(self.__name, self.__age,self.__branch, self.__account_no,self.__balance))
            con.commit()
            c.close()
            con.close()
            logging.info("Your bank account successfully created")
        except Exception as e:
            logging.error(f"Enter valid details {e}")
    @staticmethod
    def fetch_details(account_no: str)-> "Bank | None":
        """fetches data from the oracle database"""
        try:
            dsn=cx_Oracle.makedsn("localhost",1521,service_name="orcl")
            con=cx_Oracle.connect(user="tharun",password="tharun",dsn=dsn)
            c=con.cursor()
            c.execute(""" select name, age, branch, account_no, balance from bank_management where account_no= :1 """,(account_no.strip(),))
            row=c.fetchone() #fetches the maching row
            c.close()
            con.close()
            if row:
                name, age, branch, acc_no, balance = row
                return Bank(name, age, branch, acc_no, balance)
            else:
                logging.error("no account found")
                return None
        except Exception as e:
            logging.error(f"invalid data {e}")
            return None
    def update_balance(self) -> None:
        """updating the balance in database"""
        try:
            dsn=cx_Oracle.makedsn("localhost",1521,service_name="orcl")
            con=cx_Oracle.connect(user="tharun",password="tharun",dsn=dsn)
            c=con.cursor()
            c.execute("""update bank_management set balance = :1 where account_no= :2""",(self.__balance,self.__account_no))
            con.commit()
            c.close()
            con.close()
            logging.info("your balance updated")
        except Exception as e:
            logging.error(f"invalid {e}")