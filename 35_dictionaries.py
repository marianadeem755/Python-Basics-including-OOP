# dict={"Maria":50,"Shazia":55,"tuba":90,"javeria":59}
dict={"Maria":50,"Shazia":55,"tuba":90,"javeria":59}
print(dict.get("Maria"))
print(dict["Maria"])
print(dict["Maria"])
print(dict["Shazia"])
print(dict["tuba"])
print(dict["javeria"])
dic={57:"Maria",65:"Shazia",90:"tuba",79:"javeria"}
print(dic[57])
print(dic[79])
print(dic[90])
print(dic[65])
print(dic.items())
print(dic.keys())
print(dic.values())
for key,value in dic.items():
    print(f"The value for the key {key} is: {value}")
    print(f"The key for the value {value} is: {key}")

dictr={"Maria":"sis","Shazia":"mom","tuba":"friend","javeria":"czn"}
for key,value in dictr.items():
    print(f"The value for the key {key} is: {value}")
    print(f"The key for the value {value} is: {key}")
