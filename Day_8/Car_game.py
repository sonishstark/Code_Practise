prompt = ""
#learned how to use boolean 
while  True:
    #get input in lowercase
    prompt = input('Enter the prompt ').lower()
    if prompt == 'start':
        print('car started... Ready to go!')
    elif prompt == 'stop':
        print('Car stopped')
    elif prompt == 'help':
         print("""
start - to start the car
stop - to stop the car
quit - to quit      
               """)
    elif prompt == 'quit':
        break
    else:
        print("Sorry, I don't understand that")

#print('process finished')