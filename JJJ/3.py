import json
#parsing
with open(r'C:\Users\orynb\Desktop\lab 4\sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

imdata = data["imdata"]
for entry in imdata:
    attributes = entry["l1PhysIf"]["attributes"]
    print("{:<50}{:<20}{:<8}{:<6}".format(attributes.get('dn', ''), attributes.get('description', ''), attributes.get('speed', 'inherit'), attributes.get('mtu', '')))