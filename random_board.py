#!/usr/bin/env python3
import sys, random

random.seed(int(sys.argv[1]))

number_of_moves = int(sys.argv[2])
goal = sys.stdin.read()
goal = goal.replace(" ", "")
goal = goal.replace("\n", "")
starting_board = list(goal)
index_of_blank = 0



for i in range(number_of_moves):
    move = random.randrange(4)
    if(move == 0):
        if(index_of_blank != 0 and index_of_blank != 1 and index_of_blank != 2):
            starting_board[index_of_blank], starting_board[index_of_blank -3] = starting_board[index_of_blank -3], starting_board[index_of_blank]
            index_of_blank = index_of_blank - 3;
        
    elif(move == 1):
        if(index_of_blank != 6 and index_of_blank != 7 and index_of_blank != 8):
            starting_board[index_of_blank], starting_board[index_of_blank +3] = starting_board[index_of_blank +3], starting_board[index_of_blank]
            index_of_blank = index_of_blank + 3;
            
    elif(move == 2):
        if(index_of_blank != 0 and index_of_blank != 3 and index_of_blank != 6):
            starting_board[index_of_blank], starting_board[index_of_blank -1] = starting_board[index_of_blank -1], starting_board[index_of_blank]
            index_of_blank = index_of_blank - 1;
        
    else:
        if(index_of_blank != 2 and index_of_blank != 5 and index_of_blank != 8):
            starting_board[index_of_blank], starting_board[index_of_blank +1] = starting_board[index_of_blank +1], starting_board[index_of_blank]
            index_of_blank = index_of_blank + 1;
    
    
for i in range(len(starting_board)):
    print(starting_board[i], end='')