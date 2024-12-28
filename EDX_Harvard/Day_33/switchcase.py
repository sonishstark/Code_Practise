name = input("what's your name? ").lower()
#we can check the names this way too

def ifelse():
    
    if name in ["harry", "hermione", "ron"]:
        print("Gryffindor")
    elif name == "draco":
        print("Slytherin")
    else:
        print("Who?")
        
#ifelse()

def switchcase():
    
    match name:
        case "harry" | "hermione" | "ron":
            print("Gryffindor")
        case "draco":
            print("Slytherin")
        case _:
            print("Who?")
switchcase()