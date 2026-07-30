import random
board=[" "]*7
while True:
    print(board)
    move=int(input("Choose column (0-6): "))
    board[move]="X"
    print(board)
    if board.count("X")==4:
        print("Player Wins")
        break
    ai=random.choice([i for i in range(7) if board[i]==" "])
    board[ai]="O"
    print("AI Move")
    if board.count("O")==4:
        print("AI Wins")
        break
