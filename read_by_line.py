# WRITE A PROGRAM TO READ A TEXT FILE LINE BY LINE AND DISPLAY EACH WORD SEPARATED BY A #.
# Input File Name

print("\n\nEnter the name of the file : ")
name=str(input())
file=open(name,"r")
file.seek(0)
lines=file.readlines()
file.close()

# Replacing Empty Spaces With '#'
for line in range(0,len(lines)):
    lines[line]=lines[line].replace(" ","#")

    # Displaying Output
    print("\n\n",lines[line],end="")