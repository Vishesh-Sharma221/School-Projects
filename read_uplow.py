# Input File Name
print("\n\nEnter the name of the file : ")
file_name=str(input())
with open(file_name,"r") as file:
    file.seek(0)
    lines=file.read()

count_upper=0
count_lower=0
    
# Checking For Uppercase and Lowercase Letters
for items in lines:
    if items.isupper():
        count_upper+=1
    elif items.islower():
        count_lower+=1

# Displaying Output
print("\n\nThe number of uppercase letters in your sentence is : " + str(count_upper))
print("The number of lowercase letters in your sentence is : " + str(count_lower))