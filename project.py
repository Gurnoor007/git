
from random import random
import secrets

passwordLength=int(input("Enter password length(Minimum 12):"))
if passwordLength<12:
    print ("Invalid")
digits="0123456789"
specialCharacters="!@#$%&*"
LowerCase="qwertyuiopasdfghjklzxcvbnm"
UpperCase="QWERTYUIOPASDFGHJKLZXCVBNM"
Concatenation=digits+specialCharacters+LowerCase+UpperCase
  
while True:
   password=""
   for i in range(passwordLength):
    password += secrets.choice(Concatenation)
   if (any(char in specialCharacters for char in password) and 
    sum(char in digits for char in password)>=2 and
    any(char in LowerCase for char in password) and
    any(char in UpperCase for char in password)and
    (len(password)>=12)):
    break
print(password)


