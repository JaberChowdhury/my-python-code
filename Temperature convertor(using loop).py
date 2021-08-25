# This is temperature converator with some formula and if else statement
# °F =  9 / 5(°C) + 32
# °F = 9 / 5(K - 273) + 32
# °C = 5 / 9 (°F - 32)
# K =  ° C + 273
# °C = K - 273
# K = 5 / 9(°F - 32) + 273
print ("This is a Temperature converator and also a calculator :")
take = """
   Select your input unit ;
             [1] °F
             [2] °C
             [3]  k
             
            """ 
print (take)
temp = int(input("Enter 1,2 or 3 :- "))
print ("   ")
while True :    
    if temp == 1 :
        F = int(input("Enter the Temperature in °F unit :- "))
        C = 5 / 9 * (F - 32)
        K = 5 / 9 * (F - 32) + 273
        print (" ● Temperature, " + "°C = " + str(C))
        print (" ● Temperature, " + " K = " + str(K))
        print ("    ")
        continue
    if temp == 2 :
        C = int(input("Enter the Temperature in °C unit :- "))
        F =  9 / 5 * (C) + 32
        K =  C + 273
        print (" ● Temperature, " + "°F = " + str(F))
        print (" ● Temperature, " + " K = " + str(K))
        print ("    ")
        continue
    if temp == 3 :
        K = int(input("Enter the Temperature in K unit :- "))
        C = K - 273
        F = 9 / 5 * (K - 273) + 32
        print (" ● Temperature, " + "°C = " + str(C))
        print (" ● Temperature, " + "°F = " + str(F))
        print ("    ")
        continue
    else :
        print ("⛔⛔⛔WRONG INPUT⛔⛔⛔")
        break
        
    
    
    
    
    