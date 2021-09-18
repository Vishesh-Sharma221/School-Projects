# Taking An Input Sentence From User
string=input("\n\nEnter a sentence : ")
count_upper=0
count_lower=0

# Checking For Uppercase and Lowercase Letters
for items in string:
    if items.isupper():
        count_upper+=1
    elif items.islower():
        count_lower+=1

# Displaying Output
print("\n\nThe number of uppercase letters in your sentence is : ", count_upper)
print("The number of lowercase letters in your sentence is : ", count_lower)