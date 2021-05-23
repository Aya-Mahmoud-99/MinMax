from TicTacToe import Game

state=[]
state.append(3)
state.append([])
state.append([])
state.append([])
for i in range(3):
    for j in range(3):
        state[3].append((i,j))
end=False
game=Game()
while not end:
    a=input("Enter an action please in format of 0,1 where 0 is row 1 is column")
    action=tuple(int(x) for x in a.split(","))
    print(action)
    print(state)
    state=game.get_successor(state,action)
    print(action)
    print(state)
    end,winner=game.is_terminal(state)
print(winner)



