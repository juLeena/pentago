def put_and_spin(player,game,select1,select2,direction):
        stone=''
        if player=='흑돌':
            stone='●'
        elif player=='백돌':
            stone='○'
        if game[select1[0]][select1[1]][select1[2]]=='●' or game[select1[0]][select1[1]][select1[2]]=='○':
            return '다시'
        else:
            game[select1[0]][select1[1]][select1[2]]=stone
            if direction=='시계 방향':
                direction=1
            elif direction=='반시계 방향':
                direction=3
            for i in range(direction):
                new=[[0]*3 for i in range(3)]
                for j in range(3):
                    for k in range(3):
                        new[k][-j-1]=game[select2][j][k]
                game[select2]=new
            return game

def checking_make(check):
    checking=[]
    checkline=[]
    checkline2=[]
    checkline3=[]
    for i in range(6):
        check2=[]
        for j in range(6):
            check2.append(0)
        checking.append(check2)               
    for i in range(2):
        checkline.append(check[i])
    for i in range(3):
        for j in range(2):
            for k in range(3):
                checkline3.append(checkline[j][i][k])
    for i in range(len(checkline3)):
        checkline2.append(checkline3[i])
    checkline=[]
    checkline3=[]
    for i in range(2,4):
        checkline.append(check[i])
    for i in range(3):
        for j in range(2):
            for k in range(3):
                checkline3.append(checkline[j][i][k])
    for i in range(len(checkline3)):
        checkline2.append(checkline3[i])
    for i in range(6):
        for j in range(6):
            checking[i][j]=checkline2[i*6+j]
    return checking

def check_win(player,checking):
    if player=='흑돌':
        stone='●'
    elif player=='백돌':
        stone='○'
    for i in range(len(checking)):
        checktime=0
        for j in range(len(checking[0])):
            if checking[i][j]==stone:
                checktime+=1
            else:
                break
        if checktime==5:
            return 'win'
        checktime=0
    for i in range(len(checking)):
        checktime=0
        for j in range(len(checking[0])):
            if checking[j][i]==stone:
                checktime+=1
            else:
                break
        if checktime==5:
            return 'win'
    for i in range(2):
        checktime=0
        for j in range(6-i):
            if checking[i+j][j]==stone:
                checktime+=1
            else:
                break
        if checktime==5:
            return 'win'
    for i in range(2):
        checktime=0
        for j in range(6-i):
            if checking[j][5-(i+j)]==stone:
                checktime+=1
            else:
                break
        if checktime==5:
            return 'win'
    checktime=0
    for i in range(5):
        if checking[1+i][i]==stone:
            checktime+=1
        else:
            break
    if checktime==5:
        return 'win'
    checktime=0
    for i in range(5):
        if checking[1+i][5-i]==stone:
            checktime+=1
        else:
            break
    if checktime==5:
        return 'win'        