name = input("enter the name")
age = int(input("enter age"))
clas = int(input("enter the clas"))
phy = int(input("enter the marks in physics"))
che = int(input("chemistry marks"))
bio = int(input("biologyb marks"))
ss = int(input("social science marks"))
eng = int(input("english marks"))
hin = int(input("hindi marrks"))
sum = phy+bio+che+ss+eng+hin
per = (sum/600)
print("hello " + name)
print("you have scored" , per )


