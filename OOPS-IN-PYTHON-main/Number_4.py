# python Gross pay calculator

# We shall create a function and this will help us compute the Gross pay
def Gloss_pay(Hours,Rate):
    gross_pay = Hours * Rate
    return gross_pay
# Created a main fuction this will help me organize my code 
def main():
    #Here am prompting the user to enter hours works 
    Hours=float(input("Enter the number of hours worked: "))
    # Here am prompting the user to enter their rate of pay
    Rate=float((input("Enter the rate of pay: ")))
    #I will evoke my Gross_pay using  the print function since its a return function
    print("GrossPay:","$",Gloss_pay(Hours,Rate))
main() 
