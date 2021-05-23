##3 empty
import copy
class Game:
    def get_actions(self,state):
        return state[3]
    def is_terminal(self,state):
        if len(state[3])==0:
            return True, "draw"
        p1_tiles=state[1]
        p2_tiles=state[2]
        sums=[]
        #N*(N2+ 1)/2.
        target=state[0]*(state[0]**2+1)/2
        print(target)
        for tile in p1_tiles:
            for i in range(len(sums)):
                currSum=sums[i]
                print(currSum)
                count=currSum[1]
                value=currSum[0]
                print(value)
                if count==2 and value+tile==target:
                    return True,"p1"
                elif value>=target:
                    sums.pop(i)
                else:
                    sums.append((value+tile,count+1))
            sums.append((tile, 1))
        sums=[]
        for tile in p2_tiles:
            for i in range(len(sums)):
                print(tile+value)
                currSum=sums[i]
                count=currSum[1]
                value=currSum[0]
                if count==2 and value+tile==target:
                    return True,"p2"
                elif value>=target:
                    sums.pop(i)
                else:
                    sums.append((value+tile,count+1))
            sums.append((tile, 1))
        return False,""
    def get_successor(self,state,action,player=1):
        state1 = copy.deepcopy(state)
        if len(state[1])>len(state[2]):
            player=2
        state1[player].append(action)
        state1[3].remove(action)
        return state1






