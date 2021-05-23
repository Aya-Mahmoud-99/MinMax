import copy
class minmax:
    def minmax(self,state,game,player):
        state1 = copy.deepcopy(state)
        if player==0:
           result=self.maxvalue(state1,game)
        else:
           result = self.minvalue(state1, game)
        return result[1]
    def maxvalue(self,state,game):
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
        for currAction in actions:
            successor=game.get_successor(state1,currAction)
            result=self.minvalue(successor, game)
            if result[0]>max[0]:
                max=(result[0],currAction)
        return max
    def minvalue(self,state,game):
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
        for currAction in actions:
            successor=game.get_successor(state1,currAction)
            result=self.maxvalue(successor, game)
            if result[0]<min[0]:
                min=(result[0],currAction)
        return min


