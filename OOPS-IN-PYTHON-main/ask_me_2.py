from traceback import print_tb

# A programme that validates name if no name entered it will display hello stranger
def greet(name):
#  Use an else if to check for the empty strings
  if name=="":
      print("Hello stranger")
  else:
       print("Hello, " + name + ". Good morning!") 
def main():
    name=str(("Enter your name"))
    greet(name)
main