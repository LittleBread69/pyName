
def Name(x):
    l = []
    
    if type(x) == str:
        print(type(x))
        for i in x:
            l.append(i)
        print(l)
    elif type(x) == list:
        print(type(x))

Name("car")
Name(['dog', 'cat', 'lizard', 'my brother'])
