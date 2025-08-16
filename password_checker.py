import sys



def check_password(password):
   with open('common_password.txt','r') as f:
     common=f.read().splitlines()
   if password in common :
     return True
   
   else :
     return False


   
special_chars = "!@#$%^&*()-_+=[]{}|;:'\",.<>?/"

def password_strength(password):

  points=0
  length=len(password)
  upper = any(c.isupper() for c in password)
  lower=any(c.islower() for c in password)
  digit=any(c.isdigit() for c in password) 
  special=any(c in special_chars for c in password)
  test=[upper,lower,digit,special]
  for c in test:
    if c== True:
       points+=1
  if length>=8:
     points+=1
 

  if points<=1 :
   return f"\nVery Weak password , - score: {points}/5", points
  elif 1<points<=3 :
   return f"\nWeak password , - score: {points}/5", points
  elif points==4 :
   return f"\nGood  password , - score: {points}/5", points
  else :
   return f"\n Strong password , - score: {points}/5", points
 
def feedBack(password) :

  feedback,score=password_strength(password)

  if score<5 :
    print("______Suggestions for your password|_________\n")

    if not any(c.isupper() for c in password) :
      feedback+= "\n- Add uppercase - "
    if not any(c.islower() for c in password) :
      feedback+= "\n- Add lowercase - "
    if not any(c.isdigit() for c in password) :
      feedback+= "\n- Add digit(1,2,3...) - " 
    if not any(c in special_chars for c in password):
       feedback+= "\n- Add special characters($%^&*) - " 
    if len(password)<8 :
       feedback+= "\n- Password length migth be over 8 characters!!!" 
       
  return feedback
  
def main():
  print("\n============PASSWORD COMPLEXITY CHECKER=========\n")
  password=input("Enter your password\n")
  
  if check_password(password):
     print("!!!!This password appears in the list of common password please change it using a more secure one,  score=0/5\n")
     sys.exit()
   
  feedback=feedBack(password)
  print("\n",feedback)
if __name__=="__main__":
    main()
