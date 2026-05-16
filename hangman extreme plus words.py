import random

HANGMAN_PICS = [r'''
  +---+
      |
      |
      |
     ===''', r'''
  +---+
  O   |
      |
      |
     ===''', r'''
  +---+
  O   |
  |   |
      |
     ===''', r'''
  +---+
  O   |
 /|   |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
 /    |
     ===''', r'''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

words = '''limp jive tiki jerk halo hurl tempt creed expel yodel omega forge fluke surge alpha vista brawl snarl spasm plump shunt whirl disco tatter natter patter jabber jargon cackle pirate potato wizard freaky mosaic portal zebras squeal vermin versus wicred wicked butter bounce office wobble iphone gossip shimmy scurry liquid autopsy anxiety parsley warthog sandbox latrine plaster phantom spartan trapeze hoedown blunder tweedle twister popcorn vendetta momentum pathetic manifest saturday katamari ricochet pathetic shambles assassin firewall jeopardy zzyzzyxx detective terminate mezzanine harddrive quicktime trebuchet messenger bleachers dimension mozarella barbarian hourglass voracious newgrounds television stewardess somersault screenshot salmonella barbershop omnipotent armorgames flatulence fabrication multiplayer encyclopedia photographer marksmanship whisk shout sloth harsh rusty smash snail nepal crime enter greed camel raven gecko again train flask range altar cheek pygmy myrrh khaki larynx rhythm action answer animal israel baboon number united family konami falcon canyon jasper pompom engulf engine utopia gazebo vortex zenith aurora otiose eminem friday sunday monday tuesday buzzard jubilee cryptic croquet agility against advance android highway tainted beyonce awkward windows acronym giraffe gorilla painter ancient bellboy crimson thereby paradox trochee believe swiftie ovation hegemon mexican sastruga thursday graduate republic brandish amortize nintendo phantasm quixotic scorpion outraise wardrobe brainiac beaucoup familiar military ministry astrolabe bumblebee ephemeral facsimile labyrinth explosion expulsion hatchling violinist programme singapore classmate wednesday emojiband videotape passenger minecraft etymology mythology defection obedience evergreen insolence pneumonia quizzical aerosmith mineshaft microsoft powerpuff energetic blackpink jamiroquai stronghold kazakhstan earthquake generation chimpanzee evacuative whitesnake appreciate auditorium taylor-swift questionary quincuncial renaissance dangerously quoteworthy paleobotany extortioner idiographic macrocosmic nonflexible handwrought bowsmanship duplication enchantment telekinesis anticipation championship onomatopoeia reproduction extravaganza kindergarten satisfaction generational weatherproof comprehensive functionality perpendicular ventriloquist parallelogram boustrophedon globalization dangerousness illogicalness obstructional vegetarianism yachtsmanship'''.split()
def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter or -.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter or -.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz-':
            print('Please enter a LETTER or -.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N   E X T R E M E   P L U S   W O R D S')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'Yes! The secret word is "{secretWord}"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(f'You have run out of guesses!\nAfter {len(missedLetters)} missed guesses and {len(correctLetters)} correct guesses, the word was "{secretWord}"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break


