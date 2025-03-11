# Exception handling
# - programming errors
# - user errors
# TRY
#   <statement>
# EXCEPT
#   <statement>
# ENDTRY

def safe_student_open(filename):
  try:
    sfile = open(filename, 'rb')
    sfile.close()
  except OSError:
    print("wtf is this file man")

def test_input_integer():
  val = input("sample input: ")
  try:
    value = int(val)
    print(value)
    print("It is an integer")
  except ValueError:
    print("Noooo bro it isn't an integer cmon man get good")
# test_input_integer()

def integer(num):
  try:
    b = int(num)
    print(b)
    print("is integer")
  except:
    print("not")
safe_student_open("thing.data")p