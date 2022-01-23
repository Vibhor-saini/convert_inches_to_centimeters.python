num = int(input("Enter the lenghth in inches: "))
def CM(num):                          # Function declaration
    """ This  is a function which will convert inches to centimeters""" 
    return (num*(2.54))
    num = inch
k = CM(num)                            # Function call
print(f"{num} inches in centimeters is = {str(k)} centimeters")

# print(CM.__doc__)
             # or 


num = int(input("Enter temperature in celcious : "))
def farh(cel):
    """ This  is a function which will convert celcius to faranhiest """
    return(cel *(9/5)) + 32
f = farh(num)
print(f"Temprerature  of  {num}' celcius in faranhiet is = {str(f)}' faranhiet")