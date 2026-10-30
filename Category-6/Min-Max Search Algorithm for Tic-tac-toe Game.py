# Play Tic-Tac-Toe against a Minimax AI. Human = X; computer = O.
board=[" "]*9
wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def winner(b):
    for a,c,d in wins:
        if b[a]==b[c]==b[d]!=" ": return b[a]
def minimax(b,maximizing):
    w=winner(b)
    if w=="O": return 1
    if w=="X": return -1
    if " " not in b: return 0
    scores=[]
    for i in range(9):
        if b[i]==" ":
            b[i]="O" if maximizing else "X"
            scores.append(minimax(b,not maximizing)); b[i]=" "
    return max(scores) if maximizing else min(scores)
def ai_move():
    best=-float("inf"); choice=None
    for i in range(9):
        if board[i]==" ":
            board[i]="O"; score=minimax(board,False); board[i]=" "
            if score>best: best,choice=score,i
    return choice
def display():
    for r in range(3):
        print(" | ".join(board[r*3:r*3+3]))
        if r<2: print("--+---+--")
print("Positions are numbered 1-9, left-to-right and top-to-bottom.")
while True:
    display()
    try: move=int(input("Your move (1-9): "))-1
    except ValueError: print("Enter a number."); continue
    if move not in range(9) or board[move]!=" ": print("Invalid move."); continue
    board[move]="X"
    if winner(board)=="X": display(); print("You win!"); break
    if " " not in board: display(); print("Draw!"); break
    choice=ai_move(); board[choice]="O"; print("Computer chooses",choice+1)
    if winner(board)=="O": display(); print("Computer wins!"); break
    if " " not in board: display(); print("Draw!"); break
