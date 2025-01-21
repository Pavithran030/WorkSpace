list=["car","van","bike","lorry"]
print(len(list))
temp=list[0]
list[0]=list[3]
list[3]=temp
print(list)