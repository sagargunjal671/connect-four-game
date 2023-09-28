
# accept the input from user
while True:
    row = int(input("Enter number of rows: "))
#check the rows must be positive
    if row < 1:
        print("Please enter positive,nonzero inter for no of rows ")
        continue
    else:
        break
    
while True:
    col = int(input("Enter number of column: "))
#checking columnes should be positive
    if col < 1:
        print("Please enter positive,nonzero inter for no of column ")
        continue
    else:
        break
    
while True:
    
    if col>=row:
        max1=col
    else:
        max1=row
   
    pi = int(input("Enter number of pieces to connect: "))
#checking pieces to connect input for positive and non zero
    if pi < 1:
        print("Please enter positive,nonzero intege for no of pieces to connect")
        continue
    elif pi>max1:
        print("we cant Achieve to this condition please enter number less than maximun i.e.column or row")
        continue    
    else:
        
        break

#class for making board of given input of rows and column
class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(col)] for _ in range(row)]
        self.turns = 0
        self.lmove = [-1, -1] # [r, c]

    def boardp(self):
        print("\n")
# Number the columns seperately to keep it cleaner
        for r in range(col):
            print(f"  ({r+1}) ", end="")
        print("\n")

# Print the slots of the game board
        for r in range(row):
            print('|', end="")
            for c in range(col):
                print("  {0}  |".format(self.board[r][c]),end="")
            print(f"\n{'-' * (col*6+1)}")
        print()

        
#indentifying the player whos turn is to be next        
    def wturn(self):
        players = [player1, player2]
        return players[self.turns % 2]

#for checking the boundries of board    
    def in_bounds(self, r, c):
        return (r >= 0 and r < row and c >= 0 and c < col)

#checking the slot is available or not
    def turn(self, column):
# Search bottom up for an open slot
        for i in range(row-1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.wturn()
                self.lmove = [i, column]
                self.turns += 1
                return True
        return False


#for chechking who is winning the game
    def winner(self):
        lrow = self.lmove[0]
        lcol = self.lmove[1]
        lletter = self.board[lrow][lcol]
        #for checking all the condition of winning horizontal,vertical,diagonal
        directions = [[[-1, 0], 0, True], 
                      [[1, 0], 0, True], 
                      [[0, -1], 0, True],
                      [[0, 1], 0, True],
                      [[-1, -1], 0, True],
                      [[1, 1], 0, True],
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]

        # Search outwards looking for matching pieces
        for a in range(pi):
            for d in directions:
                r = lrow + (d[0][0] * (a+1))
                c = lcol + (d[0][1] * (a+1))

                if d[2] and self.in_bounds(r, c) and self.board[r][c] == lletter:
                    d[1] += 1
                else:
                    # Stop searching in this direction
                    d[2] = False

        # Check possible direction pairs for '4 pieces in a row'
        for i in range(0, row, 2):
            if (directions[i][1] + directions[i+1][1] >= pi-1):
                self.boardp()
                if lletter==player1:
                    p=1
                else:
                    p=2
                #displaying which player is winning the game
                print("Hurrey!!!!Player {0} is the winner!".format(p))
                return lletter   

        # Did not find any winners
        return False

#for playing the game
def play():
    #asking user for player 1 colour choice
    player1=input("Player one, do you want red or yellow \n(r=Red or y=Yellow)? ")
    if player1=='r':
        player2='y'
    else:
        player2='r'
    # Initialize the game board
    game = Board()

    gameover = False
    while not gameover:
        game.boardp()

        # Ask the user for input, but only accept valid turns
        validmove = False
        while not validmove:
            if game.wturn()==player1:
                p=1
            else:
                p=2
            #asking user where they want to insert the piece
            user_move = input("Player {0}, what column do you want to put your piece?".format(p))
            try:
                validmove = game.turn(int(user_move)-1)
            except:
            #warning if user input other than column count
                print("Please choose a number between 1 and {0}".format(col))

        # End the game if there is a winner
        gameover = game.winner()
        
        # End the game if there is a tie
        if not any(' ' in x for x in game.board):
            print("The game is a draw..")
            return


if __name__ == '__main__':
    ch=1
    while ch==1:
       
        play()
        #asking user to play it again or not
        ch=int(input("Do you want to play again(0-no, 1-yes)? "))
        
