#CTTI_110
#M6T2_FEET TO INCHES
#JOE FRYE
#11/12/17
def feetToInches(feet):
    return feet * 12.0;
feet = float(input("Enter the number of feet to convert to inches: "))
inches = feetToInches(feet)
print("Congratulations, you've converted {} feet and converted it/them to {} inches.".format(feet,inches))
