myList = ["python", "hub"]
count = 0
for i in myList:
    
    count +=1
    myList.append(i.upper())
    if count >= 2:
        break

print(myList)