lip="himani"
li = lip.capitalize()



def cap1(name, surname):
	print name + " " + surname

cap1("prashant", "tiwari")
s = "prashant tiwari"
t = "divyam bohra"
cap1(s,t)

def cap3(name, surname):

	return name + " " + surname

def cap4(name, surname):
	fullname = name + " " + surname
	return fullname

def cap5(name, surname, branch="Etnt", fruit="mango"):
	
	return name + ' ' + surname + " : " + branch + " : " + fruit
 
surname = "prashant"
name = "tiwari"
cap1(surname,name)

c = cap3("hjgj","hgdv ga")

print c
print cap5(fruit="grapes", name="Prashant", surname = "tiwari")

