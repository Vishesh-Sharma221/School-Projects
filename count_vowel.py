# WRITE A PROGRAM TO PASS STRING TO A FUNCTION AND COUNT HOW MANY VOWELS ARE THERE.

s1 = input("Enter a string: ")

# ----------- defining the function ---------

def count_my_string(string):
    count = 0
    vowels = ["a","e","i","o","u"]
    for char in s1:
        if char.lower() in vowels:
            count += 1
    print("No. of vowels: " + str(count))

# calling the function we defined to count vowels for the string 's1'
count_my_string(s1)