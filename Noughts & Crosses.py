a = "1"
b = "     |"
c= "2"# O or X
d = "    |"
e = "3 "# O or X
f = " "
g = "-"
h = " "
i = "-"
j = " "
k = "-"
l = " "
m = "-"#
n = "4"# O or X
o = "    |"
p = "5"# O or X
q = "    |"
r = "6"# O or X
f2 = " "
g2 = "-"
h2 = " "
i2 = "-"
j2 = " "
k2 = "-"
l2 = " "
m2 = "-"#
n2 = "7"# O or X
o2 = "   |"
p2 = " 8 "# O or X
q2 = "  |"
r2 = "9"# O or X
x = 0
y = 1
print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
if x == 0:
        z = 0
        while z < 1:
                userinput = input("where do you want to put an X?")
                try:
                   val = int(userinput)
                except ValueError:
                   print("That's not an int!")
                else:
                        z =2
        if userinput == "1":
            a = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x = 1
            y = 2
        if userinput == "2":
            c = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y=2
        if userinput == "3":
            e = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "4":
            n = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "5":
            p = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "6":
            r = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "7":
            n2= "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "8":
            p2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "9":
            r2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
if y == 2:
    z = 0
    while z < 1:
                userinput = input("where do you want to put an O?")
                try:
                   val = int(userinput)
                except ValueError:
                   print("That's not an int!")
                else:
                        z =1
    if userinput == "1":
            a = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x = 0
            y=1
    if userinput == "2":
            c = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
    if userinput == "3":
            e = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
    if userinput == "4":
            n = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
    if userinput == "5":
            p = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
    if userinput == "6":
            r = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 2
    if userinput == "7":
            n2= "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 2
    if userinput == "8":
            p2 = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 2
    if userinput == "9":
            r2 = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 2
if x == 0:
        z = 0
        while z < 1:
                userinput = input("where do you want to put an X?")
                try:
                   val = int(userinput)
                except ValueError:
                   print("That's not an int!")
                else:
                        z =1
        if userinput == "1":
            a = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x = 1
            y = 2
        if userinput == "2":
            c = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y=2
        if userinput == "3":
            e = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "4":
            n = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "5":
            p = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "6":
            r = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "7":
            n2= "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "8":
            p2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
        if userinput == "9":
            r2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
#
if y == 2:
    z = 0
    while z < 1:
                userinput = input("where do you want to put an O?")
                try:
                   val = int(userinput)
                except ValueError:
                   print("That's not an int!")
                else:
                        z =1
    if userinput == "1":
            a = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x = 0
            y=1
    if userinput == "2":
            c = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
    if userinput == "3":
            e = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
    if userinput == "4":
            n = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
    if userinput == "5":
            p = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
    if userinput == "6":
            r = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
    if userinput == "7":
            n2= "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
    if userinput == "8":
            p2 = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
    if userinput == "9":
            r2 = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
#
if x == 0:
        z = 0
        while z < 1:
                userinput = input("where do you want to put an X?")
                try:
                   val = int(userinput)
                except ValueError:
                   print("That's not an int!")
                else:
                        z =1
        if userinput == "1":
            a = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x = 1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
                    
        if userinput == "2":
            c = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y=2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "3":
            e = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "4":
            n = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "5":
            p = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "6":
            r = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "7":
            n2= "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "8":
            p2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "9":
            r2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
#
if y == 2:
    z = 0
    while z < 1:
                userinput = input("where do you want to put an O?")
                try:
                   val = int(userinput)
                except ValueError:
                   print("That's not an int!")
                else:
                        z =1
    if userinput == "1":
            a = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x = 0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "2":
            c = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "3":
            e = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "4":
            n = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "5":
            p = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "6":
            r = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "7":
            n2= "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "8":
            p2 = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "9":
            r2 = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
#
if x == 0:
        z = 0
        while z < 1:
                userinput = input("where do you want to put an X?")
                try:
                   val = int(userinput)
                except ValueError:
                   print("That's not an int!")
                else:
                        z =1
        if userinput == "1":
            a = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x = 1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "2":
            c = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y=2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "3":
            e = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "4":
            n = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "5":
            p = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "6":
            r = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "7":
            n2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "8":
            p2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "9":
            r2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
if y == 2:
    z = 0
    while z < 1:
                userinput = input("where do you want to put an O?")
                try:
                   val = int(userinput)
                except ValueError:
                   print("That's not an int!")
                else:
                        z =1
    
    if userinput == "1":
            a = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x = 0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "2":
            c = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "3":
            e = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "4":
            n = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "5":
            p = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "6":
            r = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "7":
            n2= "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "8":
            p2 = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "9":
            r2 = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y = 1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
#
if x == 0:
        z = 0
        while z < 1:
                userinput = input("where do you want to put an X?")
                try:
                   val = int(userinput)
                except ValueError:
                   print("That's not an int!")
                else:
                        z =1
        if userinput == "1":
            a = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x = 1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "2":
            c = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y=2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "3":
            e = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "4":
            n = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "5":
            p = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "6":
            r = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "7":
            n2= "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "8":
            p2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
        if userinput == "9":
            r2 = "X"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
#
if y == 2:
    z = 0
    while z < 1:
                userinput = input("where do you want to put an O?")
                try:
                   val = int(userinput)
                except ValueError:
                   print("That's not an int!")
                else:
                        z =1
    if userinput == "1":
            a = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x = 0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "2":
            c = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "3":
            e = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "4":
            n = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "5":
            p = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=0
            y=1
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "6":
            r = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "7":
            n2= "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "8":
            p2 = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
    if userinput == "9":
            r2 = "O"
            print(a,b,c,d,e,"\n",f,g,h,i,j,k,l,m,"\n",n,o,p,q,r,"\n",f2,g2,h2,i2,j2,k2,l2,m2,"\n",n2,o2,p2,q2,r2,"\n")
            x=1
            y = 2
            down1 = a+n+n2
            down2 = c + p + p2
            down3 = e + r + r2
            right1 = a + c+ e
            right2 = n + p + r
            right3 = n2 + p2 + r2
            diagonal1 = a + p +r2
            diagonal2 = e + p + n2
            if down1 == "XXX":
                    print("X wins")
                    quit()
            elif down1 == "OOO":
                    print("O wins")
                    quit()
            if down2 == "XXX":
                    print("X wins")
                    quit()
            elif down2 == "OOO":
                    print("O wins")
                    quit()
            if down3 == "XXX":
                    print("X wins")
                    quit()
            elif down3 == "OOO":
                    print("O wins")
                    quit()
            if right1 == "XXX":
                    print("X wins")
                    quit()
            elif right1 == "OOO":
                    print("O wins")
                    quit()
            if right2 == "XXX":
                    print("X wins")
                    quit()
            elif right2 == "OOO":
                    print("O wins")
                    quit()
            if right3 == "XXX":
                    print("X wins")
                    quit()
            elif right3 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal1 == "OOO":
                    print("O wins")
                    quit()
            if diagonal1 == "XXX":
                    print("X wins")
                    quit()
            elif diagonal2 == "OOO":
                    print("O wins")
                    quit()
