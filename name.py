mi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ma = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def Name(x):
    y = 0
    nam = ''
    l = []

    if type(x) == str:
        if x == '':
            print("You can't input an empty str.")
        else:
            for i in x:
                l.append(i)
            for i in mi:
                y += 1
                if i == l[0]:
                    l[0] = str(ma[y - 1])
                else:
                    pass
            k = 1
            z = 0
            f = False
            while l[len(l) - k] not in ma and l[len(l) - k] not in mi:
                k += 1
            while l[len(l) - k] not in mi and l[len(l) - k] in ma:
                y = 0
                for i in ma:
                    y+= 1
                    print(y)
                    if(i == l[0] and f == False):
                        z += 1
                        f = True
                    elif(l[z] == ' '):
                        z += 1
                    elif i == l[int(z)]:
                        l[z] = str(mi[y - 1])
                        z += 1
                    else:
                        pass
            for i in l:
                nam += i
            return nam
    elif type(x) == list:
        print(type(x))
    elif type(x) != list and type(x) != str:
        print(str(type(x)) + " not supported, please input a str or a list.")
