for i in range(100):
    import random as np
    a= ("rock","paper","scissor")
    b=np.choice(a)
    player=input("Enter rock/paper/scissor to play the game: " )

    if (player not in a):
        print("Inavalid!! Enter rock/paper/scissor")

    if(player==b):
        print("It's a tie!! Generate new to continue game ")
    elif(player=="rock" and b=="paper"):
        print("Oops! The Computer Wins🙃😫")
    elif(player=="paper" and b=="scissor"):
        print("Oops! The Computer Wins🙃😫")
    elif(player=="scissor" and b=="rock"):
        print("Oops! The Computer Wins🙃😫")
        
    elif(player=="rock" and b=="scissor"):
        print("Woww! The Player Wins😇😎")
    elif(player=="scissor" and b=="paper"):
        print("Woww! The Player Wins😇😎")
    elif(player=="paper" and b=="rock"):
        print("Woww! The Player Wins😇😎")
    else:
        print("Play again !!")

    

