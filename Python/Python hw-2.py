print("The numbers from 1 to 10 except 3 and 6 ")
for i in range(1,11):
    if i==3 or i==6:
        continue
    print(i,end=" ")