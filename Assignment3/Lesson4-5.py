username="python"
password="rules"

login_try=0

while login_try < 5:
  user= input("Enter a username: ")
  pwd= input("Enter a password: ")

  if (username==user) and password==pwd:
    print("Welcome")
    break
  else:
    print("wrong credentials ")
    login_try += 1

if login_try==5:
    print("Access Denied")
