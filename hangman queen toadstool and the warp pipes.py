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

words = '''mario luigi yoshi toad toadstool the-cube yung-raja warp pipe freddie-mercury brian-may john-deacon roger-taylor queen emoji emojena textopolis santa-maria philippines osaka tokyo japan manila bangkok thailand rajamangala osaka-station tokyo-dome stadium-nasional kuala-lumpur malaysia padang padang-athletics-field marina-bay singapore secc-outdoor ho-chi-minh-city vietnam goyang-stadium gyeonggi-do south-korea gelora-bung-karno jakarta indonesia kai-tak-stadium hong-kong taipei-dome taipei omni-space beijing taiwan china power-stars plaza-fifty-five yg-entertainment kpop scorpion sub-zero goro motaro clinic exit directory fruit-thrower balmain ikea unagi walmart sephora dead-cicak-radio house kpop asian oceania mcdonalds mr-coconut promotion mochi hyung maknae concert one-up-lantern emoji-band emoji-band-k emoji-band-korean-bong pondway nissan-stadium nashville ford-field detroit us-bank-stadium minneapolis soldier-field chicago flushing-meadows-corona-park flushing mall-of-america united-states-of-america ohio-stadium columbus rogers-stadium toronto rogers-arena vancouver canada banorte-stadium mexico-city mexico papp-laszlo-budapest-sportarena budapest hungary tower-bridge london utilita-arena glasgow cardiff co-op-live manchester united-kingdom palacio-vistalegre madrid spain three-arena dublin ireland ziggo-dome netherlands barclays-arena hamburg lanxess-arena cologne olympiastadion-berlin berlin germany festhalle-frankfurt frankfurt olympiahalle munich louvre-museum france paris lotto-arena antwerp belgium unipol-arena italy royal-arena copenhagen denmark avicii-arena sweden atlas-arena lodz boleh cheem o-two-arena prague czech-republic unity-arena oslo norway arena-riga riga latvia zalgirio-arena kaunas lithuania hallenstadion zurich switzerland stadthalle vienna austria meo-arena lisbon portugal dinamo-stadium minsk belarus asia europe european teatro-coliseo santiago chile el-teatrito buenos-aires argentina santo-rock-bar santo-andre brazil estadio-nacional-de-brasilia-mane-garrincha brasilia somos-rock-festival sao-paulo curitiba north-america south-america bruce-mason auckland australia festival-hall melbourne esmore-theatre sydney canberra-theatre-centre canberra fortitude brisbane mizuho-paypay-dome fukuoka okinawa-world okinawa es-con-field-hokkaido hokkaido sprunkimas world-tour'''.split()

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


print('H A N G M A N   Q U E E N   T O A D S T O O L   A N D   T H E   W A R P   P I P E S')
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

