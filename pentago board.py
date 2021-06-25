import easygui
import pentago_function as func
game=[[['0' for j in range(3)] for i in range(3)] for k in range(4)]
while True:
    player='흑돌'
    showgame=[]
    for i in range(len(game)):
            for j in range(len(game[0])):
                for k in range(len(game[0][0])):
                    if k==2:
                        showgame.append(' '+game[i][j][k]+'       '+'\n')
                    elif j==0 and k==0:
                        showgame.append(' '+'---'+str(i)+'---'+'\n'+' '+game[i][j][k])
                    else:
                        showgame.append(' '+game[i][j][k])                     
    point=easygui.choicebox('먼저 하시는 분이 흑돌이 됩니다'+'\n'+'\n'+''.join(showgame),
                         'Pentago',
                         choices=['0,0,0','0,0,1','0,0,2','0,1,0','0,1,1','0,1,2','0,2,0','0,2,1','0,2,2','1,0,0','1,0,1','1,0,2','1,1,0','1,1,1','1,1,2','1,2,0','1,2,1','1,2,2',
                                  '2,0,0','2,0,1','2,0,2','2,1,0','2,1,1','2,1,2','2,2,0','2,2,1','2,2,2','3,0,0','3,0,1','3,0,2','3,1,0','3,1,1','3,1,2','3,2,0','3,2,1','3,2,2',
                                  'Cancel'])
    if point=='Cancel':
        break
    else:
        point2=point.split(',')
        point3=[]
        for i in point2:
            point3.append(int(i))
        spin_point=easygui.choicebox('어떤 판을 돌리시겠습니까?\n'+''.join(showgame),'Pentago',choices=['1','2','3','4'])
        spin_direction=easygui.buttonbox('어떤 방향으로 돌리시겠습니까?\n'+''.join(showgame),'Pentago',choices=['시계 방향','반시계 방향'])
        game=func.put_and_spin(player,game,point3,int(spin_point)-1,spin_direction)
        game2=func.checking_make(game)
        if func.check_win(player,game2):
            easygui.msgbox('당신이 이겼습니다!','Pentago')
            break
    player='백돌'
    showgame=[]
    for i in range(len(game)):
            for j in range(len(game[0])):
                for k in range(len(game[0][0])):
                    if k==2:
                        showgame.append(' '+game[i][j][k]+'       '+'\n')
                    elif j==0 and k==0:
                        showgame.append(' '+'---'+str(i)+'---'+'\n'+' '+game[i][j][k])
                    else:
                        showgame.append(' '+game[i][j][k])
    point=easygui.choicebox('당신은 백돌입니다'+'\n'+'\n'+''.join(showgame),
                         'Pentago',
                         choices=['0,0,0','0,0,1','0,0,2','0,1,0','0,1,1','0,1,2','0,2,0','0,2,1','0,2,2','1,0,0','1,0,1','1,0,2','1,1,0','1,1,1','1,1,2','1,2,0','1,2,1','1,2,2',
                                  '2,0,0','2,0,1','2,0,2','2,1,0','2,1,1','2,1,2','2,2,0','2,2,1','2,2,2','3,0,0','3,0,1','3,0,2','3,1,0','3,1,1','3,1,2','3,2,0','3,2,1','3,2,2',
                                  'Cancel'])
    if point=='Cancel':
        break
    else:
        point2=point.split(',')
        point3=[]
        for i in point2:
            point3.append(int(i))
        spin_point=easygui.choicebox('어떤 판을 돌리시겠습니까?\n'+''.join(showgame),'Pentago',choices=['1','2','3','4'])
        spin_direction=easygui.buttonbox('어떤 방향으로 돌리시겠습니까?\n'+''.join(showgame),'Pentago',choices=['시계 방향','반시계 방향'])
        game=func.put_and_spin(player,game,point3,int(spin_point)-1,spin_direction)
        game2=func.checking_make(game)
        if func.check_win(player,game2):
            easygui.msgbox('당신이 이겼습니다!','Pentago')
            break
    
 
    
        
    
    
    
    



