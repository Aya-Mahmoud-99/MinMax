from TicTacToe import Game
from MinMax import minmax
from alpha_bata import alphabeta
from dp_alpha_beta import dp_alphabeta

state=[]
state.append(3)
state.append([])
state.append([])
state.append([])
humanturn=int(str(input("Enter your turn")))
alphabeta_enable=int(str(input("if alpha beta enable choose 1 if dp alpha beta enable choose 2 else choose 0")))
for i in range(3):
    for j in range(3):
        state[3].append((i,j))
end=False
game=Game()
turn=0
minmax=minmax()
alphabeta=alphabeta()
dpalpha=dp_alphabeta()
while not end:
    print(state)
    if turn==humanturn:
        a=input("Enter an action please in format of 0,1 where 0 is row 1 is column")
        action=tuple(int(x) for x in a.split(","))
    else:
        if alphabeta_enable==0:
            action=minmax.minmax(state,game,turn)
        elif alphabeta_enable==1:
            action=alphabeta.alphabeta(state,game,turn)
        else:
            action=dpalpha.alphabeta(state,game,turn)



    print("hahahahahahah")
    print(action)
    print(state)
    state=game.get_successor(state,action)
    print(action)
    print(state)
    end,winner=game.is_terminal(state)
    turn=turn+1
    turn=turn%2
print(winner)



