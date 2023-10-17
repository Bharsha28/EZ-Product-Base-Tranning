hashmap={}
hashmap[10]="ten"
hashmap["seven"]=7
hashmap["Hello"]="everyone"
print(hashmap)
print(hashmap[10])
try:
    print("key o")
except:
    print("key o is not in hashmap")
del hashmap[10]
print(hashmap)
if "seven" in hashmap:
    print("key seven exist")
else:
    print("key seven is not exist")
for i in hashmap.keys():
    print(i,end=" ")