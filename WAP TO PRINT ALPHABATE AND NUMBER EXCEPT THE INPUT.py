#WAP to print alphabate and number except the input
#hackerrank test problem

def missingCharacters(s):
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

    for i in s:
        if i in a:
            a.remove(i)
    b = str(a)
    print(b)

s = input("ENTER A STRING HERE:")
d = list(s)

result = missingCharacters(d)
