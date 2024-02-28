user = input("cos:")
x=0;
tesktodtylu = ""

# palindrom
if user != "":
    for i in range(len(user)):
        x = x+1
        odtylu = user[0-x]
        tesktodtylu += odtylu

    if tesktodtylu == user:
        print("dziala")
else:
    print("nie przyjmujemy pustych tekstow")
