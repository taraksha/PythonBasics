import sys

#Generate email id from input Name

"""
####Input while start up as argument#####
full_name = sys.argv[1]

in command prompt
python3 .\\src\\userInput.py Asha (note:use one \\ instead)

"""

full_name = input("Enter your Full name: ") #Input from console

email = full_name.lower().replace(" ",".") + "@companyname.com"

print("\n--- Your Profile ---")
print( "Full Name: ", full_name)
print("Email: "+email)
