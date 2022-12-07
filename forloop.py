numbers=[12,75,150,180,145]
for i in numbers:
    if i%5==0 and i<=150:
     print(i)
    elif i>150:
     continue
    elif i>500:
     break    