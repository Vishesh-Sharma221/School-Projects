# Input File Name
print("\n\nEnter the name of the file : ")
file_name=str(input())
file=open(file_name,"r")
file.seek(0)
lines=file.readlines()

# Storing All The Lines Containing "a" In A List
elist=[]
for items in lines:
    if "a" in items:
        elist.append(items)

# Removing The Lines Containing "a" From The Original File
for items in elist:
        if items in lines:
            lines.remove(items)
with open(file_name,"w") as file:
    file.writelines(lines)
    file.close()    

# Writing The Lines Containing "a" In A New File
with open("11_movea_new.txt","w+") as new_file:
    new_file.writelines(elist)
    new_file.close()