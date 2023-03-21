def setmarker():
    symbol=['X','O']
    marker=0
    while marker!=1:
        pen=input('choose a symbol for player1(X/O):')
        mark1=pen.upper()
        if mark1 in symbol:
            symbol.remove(mark1)
            mark2=symbol[0]
            marker=1
            return(mark1,mark2)
        else:
            print("choose the correct symbol!")
    return(mark1,mark2)



def display():
    print('|',data[6],'|',data[7],'|',data[8],'|')
    print('|',data[3],'|',data[4],'|',data[5],'|')
    print('|',data[0],'|',data[1],'|',data[2],'|')



def check_win():
    if data[0]==data[1] and data[1]==data[2] and data[0]!='':
        win=True
        if win:
            if data[0]==marker1:
                winner='Player1'
            else:
                winner='Player2'
    elif data[3]==data[4] and data[4]==data[5] and data[3]!='':
        win=True
        if win:
            if data[3]==marker1:
                winner='Player1'
            else:
                winner='Player2'
    elif data[6]==data[7] and data[7]==data[8] and data[6]!='':
        win=True
        if win:
            if data[6]==marker1:
                winner='Player1'
            else:
                winner='Player2'
    elif data[0]==data[3] and data[3]==data[6] and data[0]!='':
        win=True
        if win:
            if data[0]==marker1:
                winner='Player1'
            else:
                winner='Player2'
    elif data[1]==data[4] and data[4]==data[7] and data[1]!='':
        win=True
        if win:
            if data[1]==marker1:
                winner='Player1'
            else:
                winner='Player2'
    elif data[2]==data[5] and data[5]==data[8] and data[2]!='':
        win=True
        if win:
            if data[2]==marker1:
                winner='Player1'
            else:
                winner='Player2'
    elif data[0]==data[4] and data[4]==data[8] and data[0]!='':
        win=True
        if win:
            if data[0]==marker1:
                winner='Player1'
            else:
                winner='Player2'
    elif data[2]==data[4] and data[4]==data[6] and data[2]!='':
        win=True
        if win:
            if data[2]==marker1:
                winner='Player1'
            else:
                winner='Player2'
    else:
        win=False
        winner=None
    return (win,winner)

def play(x,y):
    print(x)
    global win
    global winner
    if len(position)==0 and win==False:
        win=True
        winner="Oh..No! It's a Tie"
    else:
        pos=int(input("Choose the position:"))
        if pos in position:
            data[pos-1]=y
            position.remove(pos)
            display()
            win,winner=check_win()
            global num
            num=num+1
        else:
            print('Choose the empty position!')

def game():
    while win!=True:
        if num%2==0:
            play('Player1',marker1)
        else:
            play('Player2',marker2)
    print(f"the winnner is:{winner}")



def replay():
    global k
    global proceed
    will=input('Do you want to play again?(Y/N):')
    if will.upper()=='Y':
        k=False
        proceed=True
    elif will.upper()=='N':
        k=False
        proceed=False
    else:
        print('Choose correct response!')


proceed=True
while proceed==True:
    win=False
    winner=None
    num=0
    data=['','','','','','','','','']
    position=[1,2,3,4,5,6,7,8,9]
    marker1,marker2=setmarker()
    game()
    k=True
    while k:
        replay()

