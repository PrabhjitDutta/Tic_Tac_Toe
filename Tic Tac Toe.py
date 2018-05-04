

def displayTable(l):

    print("   {x}  |  {y}  |  {z}".format(x=l[0][0], y=l[0][1], z=l[0][2]))
    print("   {x}  |  {y}  |  {z}".format(x=l[1][0], y=l[1][1], z=l[1][2]))
    print("   {x}  |  {y}  |  {z}".format(x=l[2][0], y=l[2][1], z=l[2][2]))


def askinp():
    while True:
        try:
            c = int(input())
        except:
            print("You made a mistake!\nTRY AGAIN")
            continue
        else:
            return c


def inp():

    print("Enter the Name of the first player:")
    x = input()
    print("Enter the Name of the Second player:")
    y = input()
    print("Hello {a} and {b},\nThis is your Tic-Tac-Toe Table.\n".format(a=x, b=y))
    return x, y


def TableModX(c, l):

    i = 0
    j = 0
    count = 0

    while i < 3:
        while j < 3:

            if l[i][j] == c:
                l[i][j] = 'X'
                count += 1
                break
            else:
                pass

            j += 1
        i += 1
        j = 0
    i += 1

    if count == 1:
        return l
    else:
        print("This Position is already taken\nTRY AGAIN")
        return -1


def TableModO(c, l):

    i = 0
    j = 0
    count = 0

    while i < 3:
        while j < 3:

            if l[i][j] == c:
                l[i][j] = 'O'
                count += 1
                break
            else:
                pass

            j += 1
        i += 1
        j = 0
    i += 1

    if count == 1:
        return l
    else:
        print("This Position is already taken\nTRY AGAIN")
        return -1


def TableCheck(l):

    i = 0
    j = 0

    while i < 3:
        if l[i][j] == l[i][j+1] and l[i][j] == l[i][j+2]:
            return 1
        else:
            pass
        i += 1

    i = 0

    while i < 3:
        if l[j][i] == l[j+1][i] and l[j][i] == l[j+2][i]:
            return 1
        else:
            pass
        i += 1
    i = 0

    if l[i][j] == l[i+1][j+1] and l[i][j] == l[i+2][j+2]:
        return 1
    elif l[i][j+2] == l[i+1][j+1] and l[i][j+2] == l[i+2][j]:
        return 1
    else:
        return -1


while True:
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    tempL = l
    x, y = inp()
    displayTable(l)
    i = 0

    while i < 9:
        print("\n{a}, please enter the first position of your choice with the help of its corresponding number:".format(a=x))

        while True:
            c = askinp()
            if c not in range(0,10):
                print("It's not a Valid Number\nTRY AGAIN")
                continue
            else:
                break

        l = TableModX(c, l)

        if l == -1:
            l = tempL
            c = askinp()
            l = TableModX(c, l)
        else:
            pass
        l = tempL
        displayTable(l)
        z = TableCheck(l)

        if z == 1:
            print("\n\n{a} is the winner congrats".format(a=x))
            break
        i += 1

        if i == 9:
            print("Its a Draw")
            break
        print("\n{a}, please enter the first position of your choice with the help of its corresponding number:".format(a=y))

        while True:
            c = askinp()
            if c not in range(0,10):
                print("It's not a Valid Number\nTRY AGAIN")
                continue
            else:
                break

        l = TableModO(c, l)

        if l == -1:
            l = tempL
            c = askinp()
            l = TableModO(c, l)
        else:
            pass
        l = tempL
        displayTable(l)
        z = TableCheck(l)

        if z == 1:
            print("\n\n{a} is the winner congrats".format(a=y))
            break

        i += 1

    print("\n\nWould You like to play Again\nPress y for Yes and n for No")
    h = input()

    if h == 'y':
        continue
    else:
        quit()