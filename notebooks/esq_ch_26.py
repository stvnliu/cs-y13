import pickle
import random
DATA_FILE = "CustomerData.DAT"
class CustomerRecord:
  def __str__(self) -> str:
    return f"{self.CustomerID}"
  def __init__(self):
    self.CustomerID = random.randint(100001, 1000000) 
    self.CustomerName = ""
    self.TelephoneNumber = ""
    self.OrderValueTotal = 0
customers = [CustomerRecord() for i in range(0, 1000)]
def Hash(CustomerID: int) -> int:
  return CustomerID % 1000
CustomerData = [None for i in range(0, 1000)]
def AddRecord(Customer: CustomerRecord):
  offset = 0
  while CustomerData[Hash(Customer.CustomerID) + offset] != None:
    offset += 1
  CustomerData[Hash(Customer.CustomerID) + offset] = Customer
def FindRecord(customer_id: int) -> CustomerRecord:
  starting = Hash(customer_id)
  offset = 0
  while CustomerData[starting + offset].CustomerID != customer_id:
    offset += 1
  return CustomerData[starting + offset]
def StoreRecords(filename = DATA_FILE):
  with open(filename, 'wb') as file:
    for customer in CustomerData:
      pickle.dump(customer, file)
    file.close()
for i in range(20):
  AddRecord(CustomerRecord())
for i in range(len(CustomerData)):
  if CustomerData[i] != None:
    print(f"[{i}] {CustomerData[i]} {'-> Collision!' if Hash(CustomerData[i].CustomerID) != i else ''}")