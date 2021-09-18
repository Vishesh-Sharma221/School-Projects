# Write A Program To Pass List To A Function
# To Double The Odd Values & Half The Even Values

def main():

    # Taking Input Values From User To Put In List
    input_values=input("\n\nEnter the numeric values of the list separated by an empty space : ").split()
    l1=list(input_values)
    
    # Converting String Inside List To Integer
    for items in range(0,len(l1)):
        l1[items] = int(l1[items])
    
    def func(list):
        odd=[]
        even=[]
        
        # Doubling The Odd Values And Halving The Even Values
        for x in list:
            if x%2==0:
                x//=2
                even.append(x)
            elif x%2!=0:
                x*=2
                odd.append(x)
            else:
                continue
        
        # If Input Doesn't Contain Odd Or Even Values
        if odd==[]:
            odd.append("No Odd Value Present")
        elif even==[]:
            even.append("No Even Values Present")
        
        # Displaying Output
        print("\n\nThe odd values in the list doubled are : ", odd)
        print("The even values in the list halved are : ", even)

        # Again Or Exit
        exet=input("\n\nDo you want to count the number of times a character is present in another string? (Yes/No) : ")
        if exet.lower()=="yes":
            main()
        elif exet.lower()=="no":
            print("\n\n")
            exit()
        else:
            print("\n\n")
            exit()

    func(l1)

main()