input_str = input("Enter comma-separated numbers: ")
values = []
current = ""

for ch in input_str:
    if ch == ",":
        values.append(int(current))
        current = ""
    else:
        current += ch

if current != "":
    values.append(int(current))

print(values)
print(sum(values))