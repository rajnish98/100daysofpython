#   Calculate the multiplication and sum of two numbers

def multipication_or_sum(num1, num2):
  product = num1 * num2
  
  if product <= 1000:
    return product
  else:
    return num1 + num2
  
result = multipication_or_sum(20, 30)
print("The multipication is: ", result)

# sum of two number

result = multipication_or_sum(40, 30)
print("The sum is: ", result)
  