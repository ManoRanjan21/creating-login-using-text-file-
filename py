import re
print("-----------WELCOME TO GUVI REGISTRATION -------------")
while True:
     username=input("enter username: ")
     pattern = '^[a-zA-Z]+[@]\w+[.]\w{2,3}$'
     match=re.search(pattern,username)
     if match is None:
          print("Invalid mail")
          # break
     elif match:
        
         while True:
            password=input('enter password: ')
            flag=0

            if len(password)<6 or len(password)>16:
                 print('print must have 6 to 16 characters ')
            elif re.search(r'[!@#$%&]',password) is None:
                 print("password must have one special character ")
                 flag=1
            elif re.search(r'\d',password) is None:
                  print("passsword must contain atleast one digit")
                  flag=1
            elif re.search(r'[A-Z]',password) is None:
                  print("password must contain one capital letter")
                  flag=1
            elif (flag==0):
                 #print("valid password")
                 break
         break         
# else:
#   print("inavlid mail")

def register():
  db=open("database.txt","r")
  user=username
  pas=password
  #pas2=input("reenter")
  d=[]
  f=[]
  for i in db:
    a,b=i.split(", ")
    b=b.strip()
    d.append(a)
    f.append(b)
  data=dict(zip(d,f))
  #print(data)
  if username in d:
      print("ALREADY REGISTERED")
  else:
      db=open("database.txt","a")
      db.write(username+", "+password+"\n")
      print("REGISTRATION COMPLETED !")
register()


    
