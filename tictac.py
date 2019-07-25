import os
import sys
game=[" "," "," "," "," "," "," "," "," "]      #actual entry of x and 0 is done in this list


def print_game():
    os.system('cls')  #clear screen
    print(game[0]+" | "+game[1]+" | "+game[2])
    print("__|___|___")
    print(game[3]+" | "+game[4]+" | "+game[5])
    print("__|___|___")
    print(game[6]+" | "+game[7]+" | "+game[8])
    


def begin():
    n=2   # random vale
    count=0  #count int
    print("press 1) Player1= 'X' and Player2 = '0' \n 2) Player1= '0' and Player2 = 'X'")
    tr=int(input())   #toss
    if tr==1:
        player1='X'
        player2='0'
    else:
        player1='0'
        player2='X'
    
    while True:    #always true, we'll terminate it later
        print("Player 1's turn:")
        player(player1)
        count=count+1   #incr count
        n=check_result(player1,player2) #after each turn, check the winning cond.
        if n==1:    #if won
            sys.exit()   #terminate
        if count==9:    #instead we can create a count func...whch will do all this @_@
            print("Game draw")   #draw cond
            sys.exit()            #exit
            
            
        print("Player 2's turn:")   #else next player turn
        player(player2)
        count=count+1          #count incr
        n=check_result(player1,player2)
        if n==1:    
            sys.exit()
        if count==9:            #draw cond
            print("Game draw")
            sys.exit()         #since draw....exit
            
def player(p):
    
    print("Choose an empty space from 1-9:")
    t=int(input())
    if game[t-1] != ' ' :    #to check, wheather that pos is already filled or not(not empty)
        print("Space not empty")
        player(p)
    else:
        game[t-1]=p  #if empty, fill that space...
        print_game()  #to print ttt board (the filled pos)
        

    

def check_result(p1,p2):
    value=6   #random value
    for i in range(8):
        if game[i]== " ":  #if blank....fill 6, cuz we cant compare x ,0 will empty
            game[i]=6
    
    solution1=list(set((game[0],game[4],game[8])))  #eg [{x 0 6}]
    solution2=list(set((game[0],game[3],game[6])))  #eg [{X}] all 3 X...in set no repetition
    solution3=list(set((game[1],game[4],game[7])))
    solution4=list(set((game[3],game[4],game[5])))
    solution5=list(set((game[2],game[5],game[8])))
    solution6=list(set((game[2],game[4],game[6])))
    solution7=list(set((game[6],game[7],game[8])))
    solution8=list(set((game[0],game[1],game[2])))
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]
    
    for i in range(8):
        if len(result[i]) == 1 and result[i][0] != 6 :  #check :only one element n its not 6
            if result[i][0] == p1:      # if its equal p1,,p1 wins
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            value=5
    
    for i in range(8):
        if game[i] == 6 :
            game[i]=" "   #if no win replacing 6 again with blank values
        
    if value == 5:
        return 1
    else:
        return 2


print("The pattern for tic tac toe board is as follows:")
print(" 1 | 2 | 3 ")
print(" __|___|___")
print(" 4 | 5 | 6 ")
print(" __|___|___")
print(" 7 | 8 | 9 ")
print("   |   |   ")
begin()











 










   