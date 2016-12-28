# item.picture
a1 = '"C:\\Users\\14PR\\Desktop\\IH\\'
b1 = '.jpg"'
c1 = ' target_'
c2 = 'picture>'
d1 = 'White>'
d2 = 'Black>'
e1 = 'W'
e2 = 'B'
for j in range(1, 4):
    if j == 1:
        print(it1+c1+d1)
        a = a1+e1
    elif j == 2:
        print(it1+c1+d2)
        a = a1+e2
    else:
        print(it1+c2)
    for i in range(1, 5):
        print('   /'+str(i)+' = '+a+str(i)+b1)
    print(it2)
