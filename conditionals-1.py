name =input("Please enter your name:")
print("Hello", name , "Welcome to green Afro_Transportation! ")
should_we_buy_share = input("Do you want to buy a vaiable share?")
if should_we_buy_share == "Yes" or should_we_buy_share == "yes": 
    print("follow the following instructions")
    print("We are proudly here to help you out buying shares from Afro Trans")
    share_type = input("please enter your share type: ")
    if share_type == "Private": 
        marital_status =input("please enter your marital status: ")
        if marital_status == "Married":
            partners_name = input("please enter your partners name:")
            print("Congratulations! Your are now our respected partner.")
        else:
            print(" Attatch your unmarried certification: ")
            
    elif share_type == "Business":
        Business_type =input("Please enter your business name:")
        print("We come", {Business_type} ,"to be part of our business")
    else:
        print("please read the available options")
elif should_we_buy_share == "No" or should_we_buy_share =="no":
    Business_details = input(" Do you want to know our business details?: ")
    if Business_details == "Yes" or Business_details == "yes":
        print("here are our business details")
    elif Business_details == "No" or Business_details == "no":
        print("We recommend you to come back soon! enjoy!")
    else:
        print("Have a nice day!")
else:
    print("We hope you to come back soon! enjoy!")
    
