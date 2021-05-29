
# print(result)

# name = "Bob"
# greeting = f"Hello, {name}"

# print(greeting)

name = "Bob"
greeting = "Hello, {}"

with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")

print(with_name)
print(with_name_two)

longer_phrase = "Hello {}, Today is {}"
formatted = longer_phrase.format(name, "Monday")
print(formatted)
