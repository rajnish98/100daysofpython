def get_single_digit(number):
  if len(number) == 1 and number.isdigit():
    return True
  
  else:
    return False
  
while True:
  input_number = input("enter a number: ")
  if get_single_digit(input_number):
    print("single valid digit")
    break
  else:
    print("Not single valid digit . try again.")
    
print("single digit you enter is :", input_number)