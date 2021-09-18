# WRITE A PROGRAM TO READ A TEXT FILE AND DISPLAY THE NUMBER OF VOWELS IN THE FILE.

with open('sample.txt','r') as f:
    vowels = ["a","e","i","o","u",]
    vowel_count = 0
    content = f.read()
    for line in content:
        if line.lower() in vowels:
            vowel_count += 1

print("No. of vowels in this text file: ", vowel_count)
