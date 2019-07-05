correct_password="python123"
name=input("enter name")
surname=input("enter surname")
password=input("Enter password :")
while correct_password != password:
	password=input(" enter again Enter password :")
print ( "Hi",name,"you are logged in")
print ( "Hi %s you are logged in" %name )
message = ( "Hi",name,"you are logged in")
print(message)

message2 = "Hi %s %s you are logged in " % (name,surname)
print(message2)
