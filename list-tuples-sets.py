listExmp = ["list", "bob", "Sally"]
tupleExmp = ("list", "bob", "Sally")
# Cannot be modified
setExmp = {"list", "bob", "Sally"}
# cannot use subscript notation
# can add to a set, can't have duplicates

# print(listExmp[0])
listExmp[0] = "Smith"
# print(listExmp[0])

listExmp.append("Darryl")
listExmp.remove("bob")
# print(listExmp)

friends = {"Bob", "Rolfe", "Anne"}
classmates = {"Bob", "Anne", "Cassie"}
abroad = {"Bob", "Anne"}
others = {"Jim"}

local_friends = friends.difference(abroad)
print(local_friends)
people = friends.union(others)
print(people)
both = friends.intersection(classmates)
print(both)

print(5 == 5)
# compare
print(10 != 10)
print(11 >= 10)
