def checkLetter():
    global updatedSpaces
    if letter in word:
        checkifWon()
        updatedSpaces = updatedSpaces - 1
        
    else:
        lives = lives - 1
        getLetter() 
        
word = ("Kyle")
wordList = list(word.lower())
updatedSpaces = []
wordLen = len(word)
lives = 5
letter = " "

for i in range (0, int(wordLen)):
    updatedSpaces.append("_")
    
def getLetter():
    global letter
    letter = raw_input ("Guess a letter   ")

def check():
    global updatedSpaces
    global lives
    global letter
    for x in range(0, int(wordLen)):
        if letter == wordList[x]:
            updatedSpaces[x] = wordList[x]
            print(updatedSpaces)
            getLetter()
        else:
            lives = -1
            if lives != 0:
                print(updatedSpaces)
                getLetter()
            else:
                print("Game Over")
                
def game():
    getLetter()
    check()
    
game()              
