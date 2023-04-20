import json

file_name = "/var/log/auth.log"
file = open(file_name, "r")
data = []
order = ["month", "date", "time", "host", "program", "pam", "messages"]

for line in file.readlines():
    details = line.split(" ")
    details = [x.strip() for x in details]
    structure = {key:value for key, value in zip(order, details)}
    data.append(structure)
    
for entry in data:
    print(json.dumps(entry, indent = 4))