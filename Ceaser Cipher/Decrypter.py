import string
lis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
while True:
    encrypt = input("Enter the ciper:")
    if encrypt == "quit123":
        break
    shift = int(input("Shift by (0-25):"))
    shift = shift%27
    encrypt=encrypt.lower()
    message = ''
    for s in encrypt:
        message += lis[(lis.index(s) - shift)%27]
    print(message)
