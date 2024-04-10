
attlist = [
{
"name": "James Ori",
 "email": "j.ori @gmail.com",
"ID_number":"LC_120"
 },
{
"name": "Nana Ori",
 "email": "n.ori @gmail.com",
"ID_number":"LC_134"
 },
{
"name": "Jeba Tara",
 "email": "j.tara @gmail.com",
"ID_number":"LC_156"
 }

]



for i in attlist:
    a= (i.get("ID_number"))
    print(a)



def att():
    b=input("pls input your reg code")
    if b in a:
        print("present")
    else:
        print("not on list")
att()


