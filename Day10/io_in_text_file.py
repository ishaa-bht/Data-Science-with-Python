# my_file = open("example.txt","w")

# my_file.write("Hello World\n")
# my_file.write("I love python")

# my_file.close()

#open file with context manager
# with open("example.txt", "a") as file:
#     file.write ("\nI am learning file operation in python\n")
    
#Reading text file
with open ("example.txt","r") as file:
    content = file.readlines()

print(content)