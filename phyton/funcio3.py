def Showgreeting (userName):
   msg = f"hola {userName}, bienvenido (a)"    
   return msg

######################################## main
print ("Enter your name: ")
user_name = input()

message = Showgreeting(user_name)
print (message)

