'''mytuple=(1,2)
tuple2=(3,4)
tuple3=tuple2
tuple2=mytuple
mytuple=tuple3
#list1=list(mytuple)
#list1.insert(3,8)
#mytuple=tuple(list1)
print(mytuple)
print(tuple2)'''
#(item1,item2,item3,item4)=tuple1
#print(item1)
#print(item2)
#print(item3)
tuple1=(10,20,30,40,20)
i=0
count=0
while i<len(tuple1):
    if tuple1[i]==20:
        count+=1
        i+=1  
print(count)      