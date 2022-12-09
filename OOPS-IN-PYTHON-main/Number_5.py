# A python grading system---
def score(marks):
# We shall use a control statement to branch our code provided a certain is not reached
    if marks > 0.9:
      print("A")  
    elif marks>=0.8:
        print("B")
    elif marks >= 0.7:
        print("C")  
        
    elif marks >= 0.6:
        print("D")
    elif marks < 0.6:
        print("F")
# We shall organize our code in a the main function for easy identification  
def main():
    # Prompt the user to enter their Score
    marks=float(input("Enter score: "))
    print(score(marks))    
main()
               
       