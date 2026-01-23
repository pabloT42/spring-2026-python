spongebob = [3,7,2,8,2,10]


for i in range(len(spongebob)):
    for j in range(len(spongebob)-1):
        if spongebob[j] > spongebob[j+1]:
            spongebob[j], spongebob[j+1] = spongebob[j+1],spongebob[j]
            
            
print(spongebob)
