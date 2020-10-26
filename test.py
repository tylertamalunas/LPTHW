x = False
y = 1

def xfalse():
    global x
    if x == False:
        x = True
    else:
        print(y)


xfalse()
print(x)