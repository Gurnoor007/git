TimeSpent=int(input("Time spent in company"))
salary=int(input("Salary:"))
if TimeSpent>=10 :
 print("New salary after 10 percent Bonus=", (salary*(10/100))+salary)
elif TimeSpent>=6 and TimeSpent<10 :
 print("New salary after 8 percent bonus="(salary*(8/100)+salary)) 
else :
 print("New salary after 8 percent bonus="(salary*(5/100)+salary))
