import string
lis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', " "]
while True:
    message = input("Enter the message:")
    if message == "quit123":
        break
    shift = int(input("Shift by (0-25):"))
    shift = shift%27
    message=message.lower()
    encrypt = ''
    for s in message:
        encrypt += lis[(lis.index(s) + shift)%27]
    print(encrypt)
