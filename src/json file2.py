import json


print("----------------start---------------------")

file = "src/data3 finglish.json"


with open(file, "r") as f:
    data = json.load(f)
    #name_data = (data["size"])
print(data)    
    
for i in data:
      print(i)
 
      

print("----------------END---------------------")
      
print("----------------start-YML---------------------")

file_2 = "src/trunk.yaml"


with open(file_2, "r") as f:
    data = json.load(f)
    #name_data = (data["size"])
print(data)    
    
for i in data:
      print(i)
 
      

print("----------------END---------------------")
    
    
    
    
    
    

import random
lower_bound = 1
upper_bound = 523
random_number = random.randint(lower_bound, upper_bound)
print("Random number between", lower_bound, "and", upper_bound, "is:", random_number)

