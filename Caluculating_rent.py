

rent =int(input("Enter your hostel/flat rent="))
food =int(input("Enter the amount of food ordered is="))
electricity = int(input("enter amount spend for electricity="))
charge_per_unit =int(input("enter the charge per unit="))
persons =int(input("enter the no: persons="))


total_bill=electricity*charge_per_unit
output=(rent+food+total_bill)//persons

print("Each person will pay = "+str(output))
