def checkLetter():
    global updatedSpaces
    if letter in word:
        checkifWon()
        updatedSpaces = updatedSpaces - 1
        
    else:
        lives = lives - 1
        getLetter() 
        
