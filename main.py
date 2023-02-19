mi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ma = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def Name(x):
    y = 0
    nam = ''
    l = []
##
    if type(x) == str:
        for i in x:
            l.append(i)
        for i in mi:
            y += 1
            if i == l[0]:
                l[0] = str(ma[y - 1])
        for i in l:
            nam += i
        return nam
    elif type(x) == list:
        print(type(x))

Name("car")
Name(['dog', 'cat', 'lizard', 'my brother'])
