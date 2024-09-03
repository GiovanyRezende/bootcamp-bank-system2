import pandas as pd
from datetime import date

def menu():
  options = """Select the desired operation:

            1 = Make a withdraw
            2 = Make a deposit
            3 = See account statement
            4 = Register user
            5 = Register account
            6 = Exit program

            """
  return int(input(options))


def withdraw(*,balance,value,num_withdraw,limit_withdraw,max_withdraw,money,operat,dat):
  if num_withdraw >= limit_withdraw:
    print("Error: you achieved withdraw limit for today\n")
  elif balance == 0:
    print("You don't have money to withdraw")
  else:
    if value > balance:
      print("Error: you can not withdraw a balance higher than current balance\n")
    elif value > max_withdraw:
      print(f"Error: you can not withdraw a balance higher than R$ {max_withdraw:.2f} limit")
    elif round(value,2) > 0:
      balance -= value
      num_withdraw += 1
      money.append(f'R$ {value:.2f}')
      operat.append("Withdraw:")
      dat.append(date.today().strftime('%Y-%m-%d'))
    else:
      print("Invalid value or unknown error")
  return balance,num_withdraw

def deposit(balance,value,money,operat,dat,/):
  if round(value,2) > 0:
    balance += value
    money.append(f'R$ {value:.2f}')
    operat.append("Deposit:")
    dat.append(date.today().strftime('%Y-%m-%d'))
  else:
    print("Invalid value or unknown error")
  return balance

def statement(balance,/,*,money,operat,dat):
  statement = {'Operation':operat,'Value':money,'Date':dat}
  statement = pd.DataFrame(statement)
  if (operat == []) or (money == []) or (date.today().strftime('%Y-%m-%d') not in dat):
    print("No operations were made today")
  else:
    print(statement)
    print(f'\nFinal balance: R$ {balance:.2f}')


def register_client(users):
  cpf = input("Input the CPF: ")
  if cpf in users['cpf']:
    print("User already registered")
    return
  else:
    name = input("Input name: ")
    birthdate = input("Input birthdate (YYYY-mm-dd): ")
    users.loc[len(users.index)] = [name,cpf,birthdate]
    print("User registered with success!")

def register_account(agency,users,accounts):
  cpf = input("Input the CPF: ")
  account_num = int(input("Input account number: "))
  if cpf in users['cpf'].values:
    print("Account registered with success!")
    accounts.loc[len(accounts.index)] = [agency,account_num,cpf]
  else:
    print("Error while trying to create account")
    return

def main():
  MAX_WITHDRAW = 500.00
  balance = 0.0
  withdraw_num = 0
  WITHDRAW_LIMIT = 3
  operat = []
  money = []
  dat = []
  AGENCY = '0001'
  users = pd.DataFrame({'name':[],'cpf':[],'birthdate':[]})
  accounts = pd.DataFrame({'agency':[],'account':[],'cpf':[]})

  while True:
    option = menu()

    if option == 1:
      value = float(input("Input withdraw value: "))
      balance,withdraw_num = withdraw(
                          balance=balance,
                          value=value,
                          num_withdraw=withdraw_num,
                          limit_withdraw=WITHDRAW_LIMIT,
                          max_withdraw=MAX_WITHDRAW,
                          money=money,
                          operat=operat,
                          dat=dat)
    elif option == 2:
      value = float(input("Input deposit value: "))
      balance = deposit(balance,value,money,operat,dat)
    elif option == 3:
      statement(balance,money=money,operat=operat,dat=dat)
    elif option == 4:
      register_client(users)
    elif option == 5:
      register_account(AGENCY,users,accounts)
    elif option == 6:
      break
    else:
      print("Error: invalid value")

main()