import json
import copy
#size 0
#p1 1
#p2 2
#empty 3
class Game:
    def get_actions(self,state):
        return state[3]

    @classmethod
    def checkRowsAndCols(self,state):
        diagonalp11=True
        diagonalp12=True
        diagonalp21 = True
        diagonalp22 = True
        for i in range(state[0]):
          if [x[0] for x in state[1]].count(i)==state[0]:
              return True,"p1"
          if [x[0] for x in state[2]].count(i) == state[0]:
            return True, "p2"
          if [x[1] for x in state[1]].count(i)==state[0]:
              return True,"p1"
          if [x[1] for x in state[2]].count(i) == state[0]:
            return True, "p2"
          if (i,i) not in state[1]:
              diagonalp11=False
          if(i,i) not in state[2]:
              diagonalp12=False
          if(state[0]-i-1,i)not in state[1]:
              diagonalp21 = False
          if(state[0]-i-1,i)not in state[2]:
              diagonalp22 = False
        if diagonalp11|diagonalp21:
            return True,"p1"
        if diagonalp12|diagonalp22:
            return True,"p2"
        return False,""


    def is_terminal(self,state):
        if len(state[3])==0:
            return True, "draw"
        boolean,winner=self.checkRowsAndCols(state)
        if boolean:
            return True,winner
        return False,"draw"
    def get_successor(self,state,action,player=1):
        state1 = copy.deepcopy(state)
        if len(state[1])>len(state[2]):
            player=2
        state1[player].append(action)
        state1[3].remove(action)
        return state1


    def load_state(self,file):
        with open(file) as f:
            lst = json.load(f)
        state=[]
        i=0
        for row in lst:
            state[0]=len(row)
            j=0
            for col in row:
                if col=='x':
                    state[1].append((i,j))
                elif col=='o':
                    state[2].append((i,j))
                else:
                    state[3].append((i,j))
                j+=1
            i+=1



