from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def canMakeWord(word, hand, wordList):
    """
    Returns True if If you can construct the word from your hand. Otherwise, returns False.

    """
    valid = True
    newHand = hand.copy()
    for i in word:
        if newHand.get(i,0) > 0: #si esta en el dict, sino devuelvo 0 que no va a ser mayor que 0
            valid = True
            newHand[i] -= 1
        else:
            valid = False
            break
    return valid
    
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for e in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if canMakeWord(e, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(e, n)
            # If the score for that word is higher than your best score
            if score > maxScore:
                # Update your best score, and best word accordingly
                maxScore = score
                bestWord = e

    # return the best word you found.
    return bestWord


#
# Problem #7: Computer plays a hand
#

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    total = 0
    while calculateHandlen(hand) >0:
        # Display the hand
        print("Current Hand: "),
        displayHand(hand)
        # Ask computer for input
        newWord = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if newWord == None:
            # End the game (break out of the loop)  
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(newWord, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(newWord, n)
                total += score
                print("\""+newWord +"\" earned "+str(score)+" points. Total: "+str(total)+ " points")
                print 
                # Update the hand 
                hand = updateHand(hand, newWord)    
    print("Total score: "+str(total)+" points.")
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    def selectHumanorPC(wordList, n, choice,hand=dict()): #el ultimo argumento, la mano es opcional porque pasa cuando hubo replay pero no cuando la mano es nueva (en realidad, pasa vacia)
        humanvspc = ''
        if choice == 'n':
            hand = dealHand(n)  #solo cargo para manos nuevas, para viejas, uso el hand vieja
        while humanvspc != 'u' and humanvspc != 'c':
            humanvspc = raw_input("Enter u to have yourself play, c to have the computer play:")
            if humanvspc == 'u':                             
                playHand(hand, wordList, n)
            elif humanvspc == 'c':
                compPlayHand(hand, wordList, n)
            else:
                print "Invalid command."
        return hand
                              
    n = HAND_SIZE
    hand = dict() ##creo una hand vacia
    choice = ''
    while choice != 'e':
        choice = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        if choice == 'n':
            
            hand = selectHumanorPC(wordList, n, choice)
                                      
        elif choice == 'r':
            if hand == {}:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                selectHumanorPC(wordList, n, choice,hand)
        elif choice == 'e':
            break
        else:
            print 'Invalid command.'

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


