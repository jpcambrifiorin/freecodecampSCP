import math
class Category:
  def __init__(self,name=""):
    self.name = name
    self.ledger = []

  def deposit(self,amount,description=""):
    self.ledger.append({"amount":amount,"description":description})
  
  def withdraw(self,amount,description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount":(amount*-1),"description":description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for iter in range(len(self.ledger)):
      balance = balance + (self.ledger[iter]['amount'])
    return balance

  def transfer(self,amount,account:'Category'):
    if self.check_funds(amount):
      self.withdraw(amount,f"Transfer to {account.get_name()}")
      account.deposit(amount,f"Transfer from {self.get_name()}")
      return True
    else:
      return False
    

  def check_funds(self,amount):
    flag = True if amount<=self.get_balance() else False
    return flag 
  
  def get_name(self):
    return self.name

  def get_withdrawals(self):
    _sum=0
    for i in self.ledger:
      _sum=_sum + (i['amount'] if i['amount']<0 else 0)
    return (_sum*-1)

  def __str__(self):
    tmp=""
    tmp=f"{self.name.center(30,'*')}\n"
    for i in self.ledger:
      tmp = tmp + f"{i['description'].ljust(23,' ')[:23]}{str(round(i['amount'],2)).rjust(7,' ')}\n"
    tmp = tmp + f"Total: {self.get_balance():.2f}"
    return tmp


def create_spend_chart(categories:list):
  chart = [(str(num)+"|").rjust(4," ") for num in range(100,-1,-10)]
  # armazenando as informacoes separadas

  spend = []
  catName = []

  for it in categories:
    spend.append(it.get_withdrawals()*-1)
    catName.append(it.get_name())
  
  # modificando o nome das categorias para adicionar espaços em brancos
  maxStr = max([len(a) for a in catName])
  catName = [catN.ljust(maxStr," ") for catN in catName]
  #

  totalSpend = sum(spend)
  spend = [math.floor((sp/totalSpend)*10) for sp in spend]
  

  # criando string de bullet points a serem adicionados ao grafico
  spendB = [(spb*"o").rjust(11," ") for spb in spend]

  print(spendB)
  for i in range(10):
    for j in spendB:
      chart [i] = str(chart[i]) + f" {j[i]} " 
    chart[i]=str(chart[i])+"\n"


  retValue = "Percentage spent by category\n"
  for iter in range(len(chart)):
    retValue = retValue + chart[iter]
  
  #criando o separador com hifens
  retValue = retValue + str('\n'+" "*4 + '-'*(3*len(categories))+'-')+'\n'

  for i in range(maxStr):
    retValue = retValue + " "*4
    for j in catName:
      retValue = retValue + f" {j[i]} "
    retValue = retValue +'\n'

  return retValue
  



  