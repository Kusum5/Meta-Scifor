f = open("language.txt","r")
x = f.read()
y = x.replace("langage","language")
f = open("language.txt","w")
f.writelines(y)