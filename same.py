#  Check if the first and last number of a list is the same

def first_last_same(numberList):
  print("given list", numberList)
  
  firstName = numberList[0]
  lastName = numberList[-1]
  
  if firstName == lastName:
    return True
  else:
    return False
  
number_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(number_x))

number_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(number_y))