# Print characters from a string that are present at an even index number

user = input("Ente The number")
print("original string", user)

size = len(user)
print(size)
# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")

for i in range(0, size-1, 2):
  print("index[", i, "]", user[i])
  
  
  
  