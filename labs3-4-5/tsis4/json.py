import json
with open("C:/Users/azama/Desktop/python/tsis4/sample-data.json", "r") as read_file:
    data = json.load(read_file)




print("Interface Status ")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
#for i in range(18):
#    print(data["dn"])
data_by_user = {}
for d in range(len(data["imdata"])):
    #data_by_user[d["l1PhysIf"]=="id"] = d
#print(data_by_user)
    print(data["imdata"][d]["l1PhysIf"]["attributes"]["dn"]+"\t"+data["imdata"][d]["l1PhysIf"]["attributes"]["modTs"]+"\t"+data["imdata"][d]["l1PhysIf"]["attributes"]["speed"]+"\t"+data["imdata"][d]["l1PhysIf"]["attributes"]["mtu"])
