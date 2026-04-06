b = ["-","-","-",
    "-", "-","-",
    "-","-","-"]
curr_player = "X"
winner = None
game_run = True



def print_board(b):
    print(b[0],"|", b[1], "|", b[2])
    print("-----------")
    print(b[3], "|", b[4], "|", b[5])
    print("-----------")
    print(b[6], "|", b[7], "|", b[8])
    
def play(b):
    ind = int(input("Enter a position: "))
    if b[ind] == "-":
        b[ind] = curr_player 
    else:
        print("The posion is alrady taken")
        
def win_H(b):
    global winner
    if b[0]==b[1]==b[2] and b[0] !="-":
        winner = b[0]
        return True
    elif b[3]==b[4]==b[5] and b[3] !="-":
        winner = b[3]
        return True
    elif b[6]==b[7]==b[8] and b[6] !="-":
        winner = b[6]
        return True
def win_V(b):
    global winner
    if b[0]==b[3]==b[6] and b[0] !="-":
        winner = b[0]
        return True
    elif b[1]==b[4]==b[7] and b[1] !="-":
        winner = b[1]
        return True
    elif b[2]==b[5]==b[8] and b[2] !="-":
        winner = b[2]
        return True
def win_D(b):
    global winner
    if b[0]== b[4] == b[8] and b[0] != "-":
        winner = b[0]
        return True
    elif b[6] == b[4]== b[2] and b[6]!="-":
        winner = b[6]
        return True
def tie(b):
    global game_run
    if "-" not in b:
        print_board(b)
        print("Its a tie!!")
        game_run = False
        
def switch():
    global curr_player
    if curr_player == "X":
        curr_player = "O"
    else:
        curr_player = "X"
        
def win():
    global game_run
    if win_D(b) or win_H(b) or win_V(b):
        print(f"the player {winner} won!!")
        game_run = False

while game_run:
    print_board(b)
    play(b)
    win()
    tie(b)
    switch()
