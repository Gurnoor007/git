import random


print("1.Rock")
print("2.Paper")
print("3.Scissor")
user_input=int(input("Choose one:"))
action=["rock","paper","scissor"]
print("Your selection is",action[user_input-1])
comp_input= random.choice(action)
print("Selection of computer is",comp_input)
if action[user_input-1]==comp_input :
 print("TIE")
elif action[user_input-1]=="rock" and  comp_input=="scissor":
 print("YOU WIN")  
elif action[user_input-1]=="scissor" and  comp_input=="paper":
 print("YOU WIN")  
elif action[user_input-1]=="paper" and  comp_input=="rock":
 print("YOU WIN")     
else:
 print("YOU LOSE")    
