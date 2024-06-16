name = input("Enter a name:\n")
password = input("Enter a password:\n")


def allowed_to_attend_pythonclass(name):
    if name == "Sayoojya":
        if password == "yes":
            print("You are allowed to enter the class")
        else:
            print("NOt allowed to enter")
    else:
        print("Invalid user")


allowed_to_attend_pythonclass(name)


name = input("Enter a student name:\n")

def allowed_to_attend_python_class(name):
    match name:

        case "DELL":
            print("Dell is allowed")
        case "Shubham":
            print("Shubham is allowed")
        case "Pallavi":
            print("Pallavi is allowed")
        case _:
            print("Not Allowed")

allowed_to_attend_python_class(name)
