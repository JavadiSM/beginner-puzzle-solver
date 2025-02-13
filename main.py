from copy import deepcopy
import time

size = None
correct_order = []

def print_test(ls):
    for i in range(size):
        for j in range(size):
            print(ls[i*size+j],end=" ")
        print("")

def pretty_grid(grid):
    o = ""
    for row in grid:
        o += f'{" ".join(str(num) for num in row)}\n'  
    return o


class State:
    def __init__(self,grid,moveCordiantes:tuple=None):
        self.grid = grid
        if not moveCordiantes:
            for i in range(size):
                for j in range(size):
                    if grid[i][j] == size**2:
                        moveCordiantes = (i,j)
                        break

        self.moveCordiantes = moveCordiantes

class Node:
    def __init__(self,state,parent):
        self.state:State = state
        self.parent:State = parent
class Solver:
    def __init__(self,state):
        self.state:State = state

    def solve(self,mode,depth=2):
        if mode == "bfs":
            res = Solver.bfs(self.state)
        elif mode == "dfs":
            res = Solver.dfs(self.state)
        elif mode == "ldfs":
            res = Solver.limited_dfs(self.state,depth)
        elif mode == "ids":
            res = Solver.ids(self.state)
        if res:
            out = []
            cur:Node = res
            while cur.parent:
                out.append(cur)
                cur = cur.parent
            out = out[::-1]
            ways_str = ""
            for state in out:
                ways_str += f"{pretty_grid(state.state.grid)}\n"
            return ways_str
        else:
            return "no way"


    def actions(state:State):
        acts = []
        i = state.moveCordiantes[0] # row
        j = state.moveCordiantes[1] # column
        if i+1 <= size-1:
            t = (i+1,j)
            acts.append(t)
        if i-1 >= 0:
            t = (i-1,j)
            acts.append(t)
        if j+1 <= size-1:
            t = (i,j+1)
            acts.append(t)
        if j-1 >= 0:
            t = (i,j-1)
            acts.append(t)
        return acts

    def act(state:State,act:tuple):
        new_state:State = deepcopy(state)
        a, b = new_state.moveCordiantes[0], new_state.moveCordiantes[1]
        new_state.grid[a][b], new_state.grid[act[0]][act[1]] = new_state.grid[act[0]][act[1]], new_state.grid[a][b]
        new_state.moveCordiantes = deepcopy(act)
        return new_state
    
    def test_goal(state:State):
        a = []
        for row in state.grid:
            a.extend(row)
        return a==correct_order
    
    def bfs(state:State):
        queue = []
        queue.append(Node(state,None))
        while queue:
            cur:Node = queue.pop(0)
            if Solver.test_goal(cur.state):
                return cur
            else:
                acts = Solver.actions(cur.state)
                children = [Node(Solver.act(cur.state,action),cur) for action in acts]
                queue.extend(children)
        return None
    
    def dfs(state:State):
        stk = []
        stk.append(Node(state,None))
        while stk:
            cur:Node = stk.pop()
            if Solver.test_goal(cur.state):
                return cur
            else:
                acts = Solver.actions(cur.state)
                children = [Node(Solver.act(cur.state,action),cur) for action in acts]
                stk.extend(children)
        return None
    
    def limited_dfs(state:State,depth):
        stk = []
        stk.append((Node(state,None),0))
        while stk:
            cur,d = stk.pop()
            if Solver.test_goal(cur.state):
                return cur
            elif d>=depth:
                continue
            else:
                acts = Solver.actions(cur.state)
                children = [(Node(Solver.act(cur.state,action),cur),d+1) for action in acts]
                stk.extend(children)
        return None
        
    def ids(state:State):
        for i in range(1,+1_000_000_000):
            res = Solver.limited_dfs(state,i)
            if res:
                return res
        return None
        


def main():
    global size
    global correct_order
    mode = input("dfs bfs or ids or ldfs ?copy paste\n").lower()
    depth = 4
    if mode=="ldfs":
        depth = int(input("and depth?\n"))
    size = int(input("size of grid?\n"))
    print("enter puzzle")
    for i in range(size):
        for j in range(size):
            correct_order.append(i * size + j + 1)
    
    grid = []
    for _ in range(size):
        grid.append(list(map(int,input().split())))
    solver = Solver(State(grid))
    print(solver.solve(mode,depth))



if __name__ == '__main__':
    main()