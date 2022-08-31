#!/usr/bin/env python3

import sys, heapq, copy, math

start = sys.stdin.read()
start = list(start)
start = [[int(start[0]), int(start[1]), int(start[2])], [int(start[3]), int(start[4]), int(start[5])], [int(start[6]), int(start[7]), int(start[8])]]
goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

class PriorityQueue():
    def __init__(self):
        self.thisQueue = []
        
    def push(self, thisNode):
        heapq.heappush(self.thisQueue, (thisNode.val, -thisNode.id, thisNode))
        
    def pop(self):
        return heapq.heappop(self.thisQueue)[2]
    
    def isEmpty(self):
        return len(self.thisQueue) == 0
    
    def length(self):
        return len(self.thisQueue)
    
nodeid = 0
class node():
    def __init__(self,val, depth=0, prev=0):
        global nodeid
        self.id = nodeid
        nodeid += 1
        self.val = val 
        self.depth = depth
        self.prev = prev
        
    def setPrev(self, prev):
        self.prev = prev
        
    def setCurrentState(self, state):
        self.state = state
        return self.state
    
    def __str__(self):
        return 'Node: id=%d val=%d'%(self.id,self.val)
    
class Set():
    def __init__(self):
        self.thisSet = set()
        
    def add(self,entry):
        if entry is not None:
            self.thisSet.add(entry.__hash__())
            
    def length(self):
        return len(self.thisSet)
    
    def isMember(self,query):
        return query.__hash__() in self.thisSet


class state():
    def __init__(self, current):
        if(start[0][0] == 0):
            self.xpos = 0
            self.ypos = 0
        elif(start[0][1] == 0):
            self.xpos = 0
            self.ypos = 1
        elif(start[0][2] == 0):
            self.xpos = 0
            self.ypos = 2
        elif(start[1][0] == 0):
            self.xpos = 1
            self.ypos = 0
        elif(start[1][1] == 0):
            self.xpos = 1
            self.ypos = 1  
        elif(start[1][2] == 0):
            self.xpos = 1
            self.ypos = 2
        elif(start[2][0] == 0):
            self.xpos = 2
            self.ypos = 0
        elif(start[2][1] == 0):
            self.xpos = 2
            self.ypos = 1 
        elif(start[2][2] == 0):
            self.xpos = 2
            self.ypos = 2 
        self.tiles = current
        
    def left(self):
        if (self.ypos == 0):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos][s.ypos-1]
        s.ypos -= 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    
    def right(self):
        if (self.ypos == 2):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos][s.ypos+1]
        s.ypos += 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    
    def up(self):
        if (self.xpos == 0):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos-1][s.ypos]
        s.xpos -= 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    
    def down(self):
        if (self.xpos == 2):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos+1][s.ypos]
        s.xpos += 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    
    def __hash__(self):
        return (tuple(self.tiles[0]),tuple(self.tiles[1]),tuple(self.tiles[2]))
    
    def __str__(self):
        return '%d %d %d\n%d %d %d\n%d %d %d\n'%(
                self.tiles[0][0],self.tiles[0][1],self.tiles[0][2],
                self.tiles[1][0],self.tiles[1][1],self.tiles[1][2],
                self.tiles[2][0],self.tiles[2][1],self.tiles[2][2])
    
    def copy(self):
        s = copy.deepcopy(self)
        return s

    
def first_choice():
    V = 0
    N = 0
    b = 0
    d = 0
    
    h = 0
    closed_list = Set()
    open_list = PriorityQueue()
    
    root = node(h)
    root.setCurrentState(state(start))
    open_list.push(root)
    expanded_node = root
    V = V+1

    
    while(expanded_node.state.tiles!=goal and not open_list.isEmpty()):
        expanded_node = open_list.pop()
        if(not closed_list.isMember(expanded_node.state)):
            V = V+1
            closed_list.add(expanded_node.state)
            weight = (expanded_node.depth+1) + h
            su = expanded_node.state.up()
            sd = expanded_node.state.down()
            sl = expanded_node.state.left()
            sr = expanded_node.state.right()
            if(su != None):
                node1 = node(weight, expanded_node.depth+1, expanded_node)
                node1.setCurrentState(su)
                open_list.push(node1)
            if(sd != None):
                node2 = node(weight, expanded_node.depth+1, expanded_node)
                node2.setCurrentState(sd)
                open_list.push(node2)
            if(sl != None):
                node3 = node(weight, expanded_node.depth+1, expanded_node)
                node3.setCurrentState(sl)
                open_list.push(node3)
            if(sr != None):
                node4 = node(weight, expanded_node.depth+1, expanded_node)
                node4.setCurrentState(sr)
                open_list.push(node4)
        
    
    
    if(expanded_node.state.tiles==goal):
        N = closed_list.length() + open_list.length()
        d = expanded_node.depth
        r = 1/d
        b = N**(r)
        path = []
        print("V=", V)
        print("N=", N)
        print("d=", d)
        print("b=", b)
        print()
        while(expanded_node!=root):
            path.append(expanded_node.state)
            expanded_node = expanded_node.prev
        path.reverse()
        for i in range(len(path)):
            print(path[i])
        
    
    
def second_choice():
    V = 0
    N = 0
    b = 0
    d = 0
    h = 0
    
    closed_list = Set()
    open_list = PriorityQueue()
   
    if start[0][1] != 1:
        h += 1
    if start[0][2] != 2:
        h +=1
    if start[1][0] != 3:
        h +=1
    if start[1][1] != 4:
        h +=1
    if start[1][2] != 5:
        h +=1
    if start[2][0] != 6:
        h+=1
    if start[2][1] != 7:
        h+=1
    if start[2][2] != 8:
        h+=1
            
            
    root = node(h)
    root.setCurrentState(state(start))
    open_list.push(root)
    expanded_node = root
    V = V+1

    
    while(expanded_node.state.tiles!=goal and not open_list.isEmpty()):
        expanded_node = open_list.pop()
        if(not closed_list.isMember(expanded_node.state)):
            V = V+1
            closed_list.add(expanded_node.state)
            su = expanded_node.state.up()
            sd = expanded_node.state.down()
            sl = expanded_node.state.left()
            sr = expanded_node.state.right()
            
            if(su != None):
                h = 0
                if su.tiles[0][1] != 1:
                    h += 1
                if su.tiles[0][2] != 2:
                    h +=1
                if su.tiles[1][0] != 3:
                    h +=1
                if su.tiles[1][1] != 4:
                    h +=1
                if su.tiles[1][2] != 5:
                    h +=1
                if su.tiles[2][0] != 6:
                    h+=1
                if su.tiles[2][1] != 7:
                    h+=1
                if su.tiles[2][2] != 8:
                    h+=1
                weight = (expanded_node.depth+1) + h
                node1 = node(weight, expanded_node.depth+1, expanded_node)
                node1.setCurrentState(su)
                open_list.push(node1)
                
            if(sd != None):
                h = 0
                if sd.tiles[0][1] != 1:
                    h += 1
                if sd.tiles[0][2] != 2:
                    h +=1
                if sd.tiles[1][0] != 3:
                    h +=1
                if sd.tiles[1][1] != 4:
                    h +=1
                if sd.tiles[1][2] != 5:
                    h +=1
                if sd.tiles[2][0] != 6:
                    h+=1
                if sd.tiles[2][1] != 7:
                    h+=1
                if sd.tiles[2][2] != 8:
                    h+=1
                weight = (expanded_node.depth+1) + h
                node2 = node(weight, expanded_node.depth+1, expanded_node)
                node2.setCurrentState(sd)
                open_list.push(node2)
            if(sl != None):
                h = 0
                if sl.tiles[0][1] != 1:
                    h += 1
                if sl.tiles[0][2] != 2:
                    h +=1
                if sl.tiles[1][0] != 3:
                    h +=1
                if sl.tiles[1][1] != 4:
                    h +=1
                if sl.tiles[1][2] != 5:
                    h +=1
                if sl.tiles[2][0] != 6:
                    h+=1
                if sl.tiles[2][1] != 7:
                    h+=1
                if sl.tiles[2][2] != 8:
                    h+=1
                weight = (expanded_node.depth+1) + h
                node3 = node(weight, expanded_node.depth+1, expanded_node)
                node3.setCurrentState(sl)
                open_list.push(node3)
            if(sr != None):
                h = 0
                if sr.tiles[0][1] != 1:
                    h += 1
                if sr.tiles[0][2] != 2:
                    h +=1
                if sr.tiles[1][0] != 3:
                    h +=1
                if sr.tiles[1][1] != 4:
                    h +=1
                if sr.tiles[1][2] != 5:
                    h +=1
                if sr.tiles[2][0] != 6:
                    h+=1
                if sr.tiles[2][1] != 7:
                    h+=1
                if sr.tiles[2][2] != 8:
                    h+=1
                weight = (expanded_node.depth+1) + h
                node4 = node(weight, expanded_node.depth+1, expanded_node)
                node4.setCurrentState(sr)
                open_list.push(node4)
        
    
    
    if(expanded_node.state.tiles==goal):
        N = closed_list.length() + open_list.length()
        d = expanded_node.depth
        r = 1/d
        b = N**(r)
        path = []
        print("V=", V)
        print("N=", N)
        print("d=", d)
        print("b=", b)
        print()
        while(expanded_node!=root):
            path.append(expanded_node.state)
            expanded_node = expanded_node.prev
        path.reverse()
        for i in range(len(path)):
            print(path[i])    

def third_choice():
    V = 0
    N = 0
    b = 0
    d = 0
    h = 0
    
    closed_list = Set()
    open_list = PriorityQueue()
   
    for i in range(1, 9):
        for j in range(3):
            for k in range(3):
                if(i == 1 and start[j][k] == 1):
                    h = h + abs((j+k)-1)
                if(i == 2 and start[j][k] == 2):
                    h = h + abs((j+k)-2)
                if(i == 3 and start[j][k] == 3):
                    h = h + abs((j+k)-1)
                if(i == 4 and start[j][k] == 4):
                    h = h + abs((j+k)-2)
                if(i == 5 and start[j][k] == 5):
                    h = h + abs((j+k)-3)
                if(i == 6 and start[j][k] == 6):
                    h = h + abs((j+k)-2)
                if(i == 7 and start[j][k] == 7):
                    h = h + abs((j+k)-3)
                if(i == 8 and start[j][k] == 8):
                    h = h + abs((j+k)-4)
                    
   
                        
    root = node(h)
    root.setCurrentState(state(start))
    open_list.push(root)
    expanded_node = root
    V = V+1

    
    while(expanded_node.state.tiles!=goal and not open_list.isEmpty()):
        expanded_node = open_list.pop()
        if(not closed_list.isMember(expanded_node.state)):
            V = V+1
            closed_list.add(expanded_node.state)
            su = expanded_node.state.up()
            sd = expanded_node.state.down()
            sl = expanded_node.state.left()
            sr = expanded_node.state.right()
            
            if(su != None):
                h = 0
                for i in range(1, 9):
                    for j in range(3):
                        for k in range(3):
                            if(i == 1 and su.tiles[j][k] == 1):
                                h = h + abs((j+k)-1)
                            if(i == 2 and su.tiles[j][k] == 2):
                                h = h + abs((j+k)-2)
                            if(i == 3 and su.tiles[j][k] == 3):
                                h = h + abs((j+k)-1)
                            if(i == 4 and su.tiles[j][k] == 4):
                                h = h + abs((j+k)-2)
                            if(i == 5 and su.tiles[j][k] == 5):
                                h = h + abs((j+k)-3)
                            if(i == 6 and su.tiles[j][k] == 6):
                                h = h + abs((j+k)-2)
                            if(i == 7 and su.tiles[j][k] == 7):
                                h = h + abs((j+k)-3)
                            if(i == 8 and su.tiles[j][k] == 8):
                                h = h + abs((j+k)-4)
                                
                weight = ((expanded_node.depth+1) + h)
                node1 = node(weight, expanded_node.depth+1, expanded_node)
                node1.setCurrentState(su)
                open_list.push(node1)
                
            if(sd != None):
                h = 0
                for i in range(1, 9):
                    for j in range(3):
                        for k in range(3):
                            if(i == 1 and sd.tiles[j][k] == 1):
                                h = h + abs((j+k)-1)
                            if(i == 2 and sd.tiles[j][k] == 2):
                                h = h + abs((j+k)-2)
                            if(i == 3 and sd.tiles[j][k] == 3):
                                h = h + abs((j+k)-1)
                            if(i == 4 and sd.tiles[j][k] == 4):
                                h = h + abs((j+k)-2)
                            if(i == 5 and sd.tiles[j][k] == 5):
                                h = h + abs((j+k)-3)
                            if(i == 6 and sd.tiles[j][k] == 6):
                                h = h + abs((j+k)-2)
                            if(i == 7 and sd.tiles[j][k] == 7):
                                h = h + abs((j+k)-3)
                            if(i == 8 and sd.tiles[j][k] == 8):
                                h = h + abs((j+k)-4)
                weight = ((expanded_node.depth+1) + h)
                node2 = node(weight, expanded_node.depth+1, expanded_node)
                node2.setCurrentState(sd)
                open_list.push(node2)
            if(sl != None):
                h = 0
                for i in range(1, 9):
                    for j in range(3):
                        for k in range(3):
                            if(i == 1 and sl.tiles[j][k] == 1):
                                h = h + abs((j+k)-1)
                            if(i == 2 and sl.tiles[j][k] == 2):
                                h = h + abs((j+k)-2)
                            if(i == 3 and sl.tiles[j][k] == 3):
                                h = h + abs((j+k)-1)
                            if(i == 4 and sl.tiles[j][k] == 4):
                                h = h + abs((j+k)-2)
                            if(i == 5 and sl.tiles[j][k] == 5):
                                h = h + abs((j+k)-3)
                            if(i == 6 and sl.tiles[j][k] == 6):
                                h = h + abs((j+k)-2)
                            if(i == 7 and sl.tiles[j][k] == 7):
                                h = h + abs((j+k)-3)
                            if(i == 8 and sl.tiles[j][k] == 8):
                                h = h + abs((j+k)-4)
                weight = ((expanded_node.depth+1) + h)
                node3 = node(weight, expanded_node.depth+1, expanded_node)
                node3.setCurrentState(sl)
                open_list.push(node3)
            if(sr != None):
                h = 0
                for i in range(1, 9):
                    for j in range(3):
                        for k in range(3):
                            if(i == 1 and sr.tiles[j][k] == 1):
                                h = h + abs((j+k)-1)
                            if(i == 2 and sr.tiles[j][k] == 2):
                                h = h + abs((j+k)-2)
                            if(i == 3 and sr.tiles[j][k] == 3):
                                h = h + abs((j+k)-1)
                            if(i == 4 and sr.tiles[j][k] == 4):
                                h = h + abs((j+k)-2)
                            if(i == 5 and sr.tiles[j][k] == 5):
                                h = h + abs((j+k)-3)
                            if(i == 6 and sr.tiles[j][k] == 6):
                                h = h + abs((j+k)-2)
                            if(i == 7 and sr.tiles[j][k] == 7):
                                h = h + abs((j+k)-3)
                            if(i == 8 and sr.tiles[j][k] == 8):
                                h = h + abs((j+k)-4)
                weight = ((expanded_node.depth+1) + h)
                node4 = node(weight, expanded_node.depth+1, expanded_node)
                node4.setCurrentState(sr)
                open_list.push(node4)
        
    
    
    if(expanded_node.state.tiles==goal):
        N = closed_list.length() + open_list.length()
        d = expanded_node.depth
        r = 1/d
        b = N**(r)
        path = []
        print("V=", V)
        print("N=", N)
        print("d=", d)
        print("b=", b)
        print()
        while(expanded_node!=root):
            path.append(expanded_node.state)
            expanded_node = expanded_node.prev
        path.reverse()
        for i in range(len(path)):
            print(path[i])    

def fourth_choice():
    V = 0
    N = 0
    b = 0
    d = 0
    h = 0
    
    closed_list = Set()
    open_list = PriorityQueue()
   
    for i in range(1, 9):
        for j in range(3):
            for k in range(3):
                if(i == 1 and start[j][k] == 1):
                    h = h + abs((j+k)-1)
                if(i == 2 and start[j][k] == 2):
                    h = h + abs((j+k)-2)
                if(i == 3 and start[j][k] == 3):
                    h = h + abs((j+k)-1)
                if(i == 4 and start[j][k] == 4):
                    h = h + abs((j+k)-2)
                if(i == 5 and start[j][k] == 5):
                    h = h + abs((j+k)-3)
                if(i == 6 and start[j][k] == 6):
                    h = h + abs((j+k)-2)
                if(i == 7 and start[j][k] == 7):
                    h = h + abs((j+k)-3)
                if(i == 8 and start[j][k] == 8):
                    h = h + abs((j+k)-4)
                    
                    
    if start[0][1] != 1:
        h += 1
    if start[0][2] != 2:
        h +=1
    if start[1][0] != 3:
        h +=1
    if start[1][1] != 4:
        h +=1
    if start[1][2] != 5:
        h +=1
    if start[2][0] != 6:
        h+=1
    if start[2][1] != 7:
        h+=1
    if start[2][2] != 8:
        h+=1 
        
    root = node(h)
    root.setCurrentState(state(start))
    open_list.push(root)
    expanded_node = root
    V = V+1

    
    while(expanded_node.state.tiles!=goal and not open_list.isEmpty()):
        expanded_node = open_list.pop()
        if(not closed_list.isMember(expanded_node.state)):
            V = V+1
            closed_list.add(expanded_node.state)
            su = expanded_node.state.up()
            sd = expanded_node.state.down()
            sl = expanded_node.state.left()
            sr = expanded_node.state.right()
            
            if(su != None):
                h = 0
                for i in range(1, 9):
                    for j in range(3):
                        for k in range(3):
                            if(i == 1 and su.tiles[j][k] == 1):
                                h = h + abs((j+k)-1)
                            if(i == 2 and su.tiles[j][k] == 2):
                                h = h + abs((j+k)-2)
                            if(i == 3 and su.tiles[j][k] == 3):
                                h = h + abs((j+k)-1)
                            if(i == 4 and su.tiles[j][k] == 4):
                                h = h + abs((j+k)-2)
                            if(i == 5 and su.tiles[j][k] == 5):
                                h = h + abs((j+k)-3)
                            if(i == 6 and su.tiles[j][k] == 6):
                                h = h + abs((j+k)-2)
                            if(i == 7 and su.tiles[j][k] == 7):
                                h = h + abs((j+k)-3)
                            if(i == 8 and su.tiles[j][k] == 8):
                                h = h + abs((j+k)-4)
                                
                if su.tiles[0][1] != 1:
                    h += 1
                if su.tiles[0][2] != 2:
                    h +=1
                if su.tiles[1][0] != 3:
                    h +=1
                if su.tiles[1][1] != 4:
                    h +=1
                if su.tiles[1][2] != 5:
                    h +=1
                if su.tiles[2][0] != 6:
                    h+=1
                if su.tiles[2][1] != 7:
                    h+=1
                if su.tiles[2][2] != 8:
                    h+=1
                                
                weight = ((expanded_node.depth+1) + h)
                node1 = node(weight, expanded_node.depth+1, expanded_node)
                node1.setCurrentState(su)
                open_list.push(node1)
                
            if(sd != None):
                h = 0
                for i in range(1, 9):
                    for j in range(3):
                        for k in range(3):
                            if(i == 1 and sd.tiles[j][k] == 1):
                                h = h + abs((j+k)-1)
                            if(i == 2 and sd.tiles[j][k] == 2):
                                h = h + abs((j+k)-2)
                            if(i == 3 and sd.tiles[j][k] == 3):
                                h = h + abs((j+k)-1)
                            if(i == 4 and sd.tiles[j][k] == 4):
                                h = h + abs((j+k)-2)
                            if(i == 5 and sd.tiles[j][k] == 5):
                                h = h + abs((j+k)-3)
                            if(i == 6 and sd.tiles[j][k] == 6):
                                h = h + abs((j+k)-2)
                            if(i == 7 and sd.tiles[j][k] == 7):
                                h = h + abs((j+k)-3)
                            if(i == 8 and sd.tiles[j][k] == 8):
                                h = h + abs((j+k)-4)
                                
                if sd.tiles[0][1] != 1:
                    h += 1
                if sd.tiles[0][2] != 2:
                    h +=1
                if sd.tiles[1][0] != 3:
                    h +=1
                if sd.tiles[1][1] != 4:
                    h +=1
                if sd.tiles[1][2] != 5:
                    h +=1
                if sd.tiles[2][0] != 6:
                    h+=1
                if sd.tiles[2][1] != 7:
                    h+=1
                if sd.tiles[2][2] != 8:
                    h+=1
                    
                weight = ((expanded_node.depth+1) + h)
                node2 = node(weight, expanded_node.depth+1, expanded_node)
                node2.setCurrentState(sd)
                open_list.push(node2)
            if(sl != None):
                h = 0
                for i in range(1, 9):
                    for j in range(3):
                        for k in range(3):
                            if(i == 1 and sl.tiles[j][k] == 1):
                                h = h + abs((j+k)-1)
                            if(i == 2 and sl.tiles[j][k] == 2):
                                h = h + abs((j+k)-2)
                            if(i == 3 and sl.tiles[j][k] == 3):
                                h = h + abs((j+k)-1)
                            if(i == 4 and sl.tiles[j][k] == 4):
                                h = h + abs((j+k)-2)
                            if(i == 5 and sl.tiles[j][k] == 5):
                                h = h + abs((j+k)-3)
                            if(i == 6 and sl.tiles[j][k] == 6):
                                h = h + abs((j+k)-2)
                            if(i == 7 and sl.tiles[j][k] == 7):
                                h = h + abs((j+k)-3)
                            if(i == 8 and sl.tiles[j][k] == 8):
                                h = h + abs((j+k)-4)
                                
                if sl.tiles[0][1] != 1:
                    h += 1
                if sl.tiles[0][2] != 2:
                    h +=1
                if sl.tiles[1][0] != 3:
                    h +=1
                if sl.tiles[1][1] != 4:
                    h +=1
                if sl.tiles[1][2] != 5:
                    h +=1
                if sl.tiles[2][0] != 6:
                    h+=1
                if sl.tiles[2][1] != 7:
                    h+=1
                if sl.tiles[2][2] != 8:
                    h+=1
                weight = ((expanded_node.depth+1) + h)
                node3 = node(weight, expanded_node.depth+1, expanded_node)
                node3.setCurrentState(sl)
                open_list.push(node3)
            if(sr != None):
                h = 0
                for i in range(1, 9):
                    for j in range(3):
                        for k in range(3):
                            if(i == 1 and sr.tiles[j][k] == 1):
                                h = h + abs((j+k)-1)
                            if(i == 2 and sr.tiles[j][k] == 2):
                                h = h + abs((j+k)-2)
                            if(i == 3 and sr.tiles[j][k] == 3):
                                h = h + abs((j+k)-1)
                            if(i == 4 and sr.tiles[j][k] == 4):
                                h = h + abs((j+k)-2)
                            if(i == 5 and sr.tiles[j][k] == 5):
                                h = h + abs((j+k)-3)
                            if(i == 6 and sr.tiles[j][k] == 6):
                                h = h + abs((j+k)-2)
                            if(i == 7 and sr.tiles[j][k] == 7):
                                h = h + abs((j+k)-3)
                            if(i == 8 and sr.tiles[j][k] == 8):
                                h = h + abs((j+k)-4)
                                
                if sr.tiles[0][1] != 1:
                    h += 1
                if sr.tiles[0][2] != 2:
                    h +=1
                if sr.tiles[1][0] != 3:
                    h +=1
                if sr.tiles[1][1] != 4:
                    h +=1
                if sr.tiles[1][2] != 5:
                    h +=1
                if sr.tiles[2][0] != 6:
                    h+=1
                if sr.tiles[2][1] != 7:
                    h+=1
                if sr.tiles[2][2] != 8:
                    h+=1
                weight = ((expanded_node.depth+1) + h)
                node4 = node(weight, expanded_node.depth+1, expanded_node)
                node4.setCurrentState(sr)
                open_list.push(node4)
        
    
    
    if(expanded_node.state.tiles==goal):
        N = closed_list.length() + open_list.length()
        d = expanded_node.depth
        r = 1/d
        b = N**(r)
        path = []
        print("V=", V)
        print("N=", N)
        print("d=", d)
        print("b=", b)
        print()
        while(expanded_node!=root):
            path.append(expanded_node.state)
            expanded_node = expanded_node.prev
        path.reverse()
        for i in range(len(path)):
            print(path[i])  
    


def main():


    hChoice = int(sys.argv[1])

    if(hChoice == 0):
        first_choice()
    
    elif(hChoice == 1):
        second_choice()
    
    elif(hChoice == 2):
        third_choice()
    
    elif(hChoice == 3):
        fourth_choice()

main()
    
