def main():
    print_column(3)
    print_row(4)
    
def print_row(width):
    print("?" * width)

def print_column(height):
    for h in range(height):
        print("#")

main()
#sb