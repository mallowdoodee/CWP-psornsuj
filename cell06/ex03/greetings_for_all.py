def greetings(name=""):
    if type(name) != str:
        print("Error! It was not a name.")
    elif name == "":
        print("Hello, noble stranger.")
    else:
        print("Hello, %s" %name)
    return

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)