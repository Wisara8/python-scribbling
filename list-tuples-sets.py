listExmp = ["list", "bob", "Sally"]
tupleExmp = ("list", "bob", "Sally")
# Cannot be modified
setExmp = {"list", "bob", "Sally"}
# cannot use subscript notation
# can add to a set, can't have duplicates

print(listExmp[0])
listExmp[0] = "Smith"
print(listExmp[0])

listExmp.append("Darryl")
listExmp.remove("bob")
print(listExmp)