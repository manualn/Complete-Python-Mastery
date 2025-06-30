point = {"x": 1, "y": 2}


point = dict(x=1, y=2)
print(point["x"])
point["x"] = 10
print(point)
# We can add a new key
point["z"] = 20
print(point)


#print(point["a"])  # KeyError

if "a" in point:
    print(point["a"])
print(point.get("a", 0))


del point["x"]
print(point)


for key in point:
    print(key, point[key])

for x in point.items():
    print(x)

# We can unpack the tuple right here
for key, value in point.items():
    print(key, value)