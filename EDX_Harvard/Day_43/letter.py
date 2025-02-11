def main():
    print(write_letter("Mario", "Princes Peach"))
    print(write_letter("Luigi", "Princes Peach"))
    print(write_letter("Daisy", "Princes Peach"))
    print(write_letter("Yoshi", "Princes Peach"))

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},
        
        you are cordially invited to a ball at
        Peach's Caste this evening, 7:00 PM.
        
        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()