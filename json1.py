import json

with open("C:\\Users\\shash\\Downloads\\Simple.json", 'r') as file:
    data = json.load(file)
    print(data)
element = data["address"]
print ("Print full address=",element)
element = data["address"]["street"]
print("Print Street=", element)

data["address"]["street"]= "854 Main St"
element = data["address"]["street"]
print("Changed address=",element)
element1 =data["skills"][0]
print(element1)

with open("C:\\Users\\shash\\Downloads\\Simple.json", 'w') as file:
    json.dump(data,file,indent=2)
    print("Access Modified data:",data)