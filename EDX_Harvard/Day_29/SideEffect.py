#global variable
emoticon = "v.v"

def main():
    #we can modify the global variable 
    global emoticon
    #passing a string to the function
    say("Is anyone there?")
    #moification only happening in the second function call
    emoticon = ":)"
    say("Oh, hi")

def say(phrase):
    print(phrase + " " + emoticon)

#since the say funciton is inside the main function you dont have to call it separately again    
main()