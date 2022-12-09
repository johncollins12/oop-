# A python name checker programme

# We have used the main () fuction to organize our code.
def main():
    # Ask the user for their name
    # Store the user's name in a variable
     name = str(input("Enter your name: "))
     
    #  Use the  if statement and nested if to validate the user's input
     if name =="Jack" or name =="Jackie":
        print("Hello,{}".format(name))
        print("Goodbye,{}".format(name))
        
     else:
        print("Hello friend!!!")
        age=int(input("Enter your age: "))
        if age < 18:
            print("You are below the the working age")
        elif age > 18 and age < 25:
            print("You are of age of working,look for a job")
        elif age>=25 and age <= 30:
            print("You  should be having a job already")
        elif age < 90 and age >= 60:
            print("You are old enough to retire") 
        else:
            print(f"Goodbye,{name},you are {age} years old and you are alien in nature") 
main()     