# update()
dic={54:89,43:90,21:34,67:32,108:965}
dic1={986:765,23:12,90:76,106:124,52:31}
dic.update(dic1)
print(dic)

# removing items from dict
del(dic[54])
print(dic)
del(dic)
print(dic)

dic.clear()
print(dic)

dic.pop(54)
print(dic)

dic.popitem()
print(dic)