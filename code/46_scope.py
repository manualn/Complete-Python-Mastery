message = "a"
def greet(name):
    global message
    message = "b"

greet("Mosh")
print(message)