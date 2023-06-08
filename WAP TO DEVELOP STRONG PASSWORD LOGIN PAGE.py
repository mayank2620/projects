import string
k = False
z = False
p = False
m = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

while 1 > 0:
    a = input("ENTER A PASSWORD:")
    b = 0
    e = len(a)
    for i in a:
        b += 1
    if b > 7:
        d = b - 7
        c = "password is more by {}"
        print(c.format(d))

    elif b < 7:
        dr = 7 - b
        c = "password is less by {}"
        print(c.format(dr))
    elif b == 7:
        for j in a:
            if j in string.ascii_uppercase:
                k = True

            elif j in string.ascii_lowercase:
                z = True

            elif j in m:
                p = True

        if (k and z and p == True):
            print("::strong password::")
            break

        else:
            print("::not strong password::")
            break