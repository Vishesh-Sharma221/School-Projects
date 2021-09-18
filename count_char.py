# WRITE A PROGRAM TO PASS STRING TO A FUNCTION AND COUNT 
# HOW MANY TIMES A PARTICULAR CHARACTER IS PRESENT IN THE STRING.

# ----------- defining the function -------------------

def count_my_string(string,char):
    count = 0
    for i in string:
        if i.lower() == char.lower():      # using .lower() to make our program not case sensitive 
            count += 1
    print("No. of times " + char + " occured in is: " + str(count))

# now we take the string and the character to search for by user

s1 = input("Enter the string: ")
ch = input("Enter the character to search: ")

count_my_string(s1,ch)
