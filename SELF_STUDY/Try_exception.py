def Use_of_Finally():
    
    try :
        a = int(input("Enter : "))
        b = int (input("Enter : "))
        
        if b==0 :
            raise ZeroDivisionError ("Numenator cant be Zero")
        else :
            return (a/b)
            
    except Exception as e :
        print(e)

    else : 
        print("Successfully Try bloack Execute \nWhen try are successfully execute then else part execute")
    finally :
        print("Succefully finally block is working \n")
        
print(Use_of_Finally())