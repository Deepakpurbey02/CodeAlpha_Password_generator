import random
import string
import time


def body():
    print("-----------------CODE ALPHA TASKS 1------------------------")
    print("\n")
    print("""                PASSOWRD GENERATOR    \n""")

def generate_password(length):
    if (length<8 or length>17 ):
        
        return " please enter  password length must be at least 8 - 16  "
        
    
    uppercase_letter = string.ascii_uppercase
    lowercase_letter = string.ascii_lowercase
    digit = string.digits
    special_letter = ["@","#","&","!"]


    password =(random.choice(uppercase_letter) + random.choice(lowercase_letter)+ random.choice(special_letter) + random.choice(digit))
    remender_length = length -3
    password += "".join(random.choice(string.ascii_letters +string.digits + string.ascii_lowercase) for _ in range(remender_length))
    
    
    
    return password
    
    
def main():
    body()
    time.sleep(1)
    try:
        password_length = int(input("Enter the length of password : "))
        password = generate_password(password_length)
        print("Generated Password : ", password)
    except ValueError:
        print("Invalid input. Please enter a valid number between 8 - 16 : ")

main()