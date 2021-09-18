# Write A Program To Display Maximum, Minimum & Mean Of Values From The Inputted List

def minean():

    # Taking Input Values From The User To Put In List
    input_list=input("\n\nEnter the numeric elements of the list separated by an empty space : ").split()

    # Converting String Inside List To Integer
    for items in range(0,len(input_list)):
        input_list[items] = int(input_list[items])

    # Calculating Minimum, Maximium, Mean Of The Values Entered
    sum_num=sum(input_list)
    min_num=min(input_list)
    max_num=max(input_list)
    mean=sum_num/len(input_list)

    # Displaying Output
    print("\n\nMinimum value of the entered numbers is = ", min_num)
    print("Maximum value of the entered numbers is = ", max_num)
    print("         Mean of the entered numbers is = ", mean)
    
    # Again Or Exit
    exet=input("\n\nDo you want to calculate maximum, minimum, and mean of values for another list? (Yes/No) : ")
    if exet.lower()=="yes":
        minean()
    elif exet.lower()=="no":
        print("\n\n")
        exit()
    else:
        print("\n\n")
        exit()

minean()