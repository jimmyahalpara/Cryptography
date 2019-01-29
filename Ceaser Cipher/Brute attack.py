import string
lis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', " "]
while True:
    cipher = input("Enter the message:")
    if cipher == "quit123":
        break
    for shift in range(27):
        cipher=cipher.lower()
        encrypt = ''
        for s in cipher:
            encrypt += lis[(lis.index(s) - shift)%27]
        print(str(shift)+' - '+ encrypt)
