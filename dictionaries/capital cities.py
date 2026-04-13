countries = ["France", "Japan", "Brazil", "Egypt"]
capitals = ["Paris","Tokyo", "Brasilia", "Cairo"]

world = {}
for i in range(len(countries)):
    world[countries[i]] = capitals[i]
    
for k in world:
    print(k, end=" ")
    
for k in world:
    print(world[k], end=" ")
