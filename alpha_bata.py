import copy
class alphabeta:
    def alphabeta(self,state,game,player):
        state1 = copy.deepcopy(state)
        if player==0:
           result=self.maxvalue(state1,game,-100000000000000000000000,1000000000000000000000000000000)
        else:
           result = self.minvalue(state1, game)
        return result[1]
    def maxvalue(self,state,game,alpha,beta):
        state1 = copy.deepcopy(state)
        boolean,winner=game.is_terminal(state1)
        if boolean:
            if winner=="p1":
                return (1,"")
            elif winner=="p2":
                return (-1,"")
            else:
                return (0,"")
        actions=game.get_actions(state1)
        max=(-100000000000000000000000000000000000000000000,actions[0])
        curralpha=alpha
        for currAction in actions:
            successor=game.get_successor(state1,currAction)
            result=self.minvalue(successor, game,curralpha,beta)
            if result[0]>max[0]:
                max=(result[0],currAction)
            if result[0]>=beta:
                return max
            if result[0]>curralpha:
                curralpha=result[0]
        return max
    def minvalue(self,state,game,alpha,beta):
        state1 = copy.deepcopy(state)
        boolean,winner=game.is_terminal(state1)
        if boolean:
            if winner=="p1":
                return (1,"")
            elif winner=="p2":
                return (-1,"")
            else:
                return (0,"")
        actions=game.get_actions(state1)
        min=(100000000000000000000000000000000000000000000,actions[0])
        currbeta=beta
        for currAction in actions:
            successor=game.get_successor(state1,currAction)
            result=self.maxvalue(successor, game,alpha,currbeta)
            if result[0]<min[0]:
                min=(result[0],currAction)
            if result[0]<=alpha:
                return min
            if result[0]<currbeta:
                currbeta=result[0]

        return min


