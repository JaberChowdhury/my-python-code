# loop programme
# with "break" and "continue"

while True :
    print ("What is your name?")
    name = input()
    if name != 'Batman' :
        print("⛔⛔⛔wrong input⛔⛔⛔")
        print ("  ")
        continue      
    print ("  ")
    
    print ("what is your passcode?")
    password = input()
    if password == 'now' :
       break
    
        