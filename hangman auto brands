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

words = '''abadal abarth abbott-detroit abt ac-automobiles acura aiways aixam alfa-romeo alpina alpine alta alvis amerian-motors-corporation apollo arash arcfox ariel aro arrival arrinera artega ascari askam aspark aston-martin atalanta auburn audi audi sport austin autobacs autobianchi axone bayerische-motoren-werke briggs-automotive-company baic-motor baojun beiben bentley berkeley berliet bertone bestune bharatbenz bitter bizzarrini borgward bowler brabus brammo brilliance bristol brooke bufori bugatti buick byd bytone cadillac camc canoo caparo carbon-motors carlsson caterham changan changfeng chery chevrolet corvette chrysler cisitalia citroen cizeta coda cole corre-la-licorne dacia daewoo daf daihatsu daimler dartz datsun david-brown dayun de-tomaso delage desoto detroit-electric devel-sixteen devon-motorworks diatto dina dkw delorean-motor-company dodge dongfeng donkervoort drako ds-automobiles duesenberg eagle edag edsel eicher elemental elfin elva englon erf eterniti exeed nine-ff facel-vega faraday-future faw jiefang ferrari fiat fioravanti fisker foden force-motors ford mustang foton fpv franklin freightliner fso guangzhou-automobile-group gardner-douglas gaz geely general-motors genesis geo geometry gilbern gillet ginetta general-motors-truck-company golden-dragon gonow great wall grinnall gumpert hafei haima haval hawtai hennessey hillman hindustan-motors higer hino hiphi hispano-suiza holden holden-special-vehicles hommell honda hongqi hongyan horch hudson hummer hupmobile hyundai hero-motocorp ic-bus international-harvester infiniti innocenti intermeccanica international invicta ikco irizar isdera iso isuzu iveco jac jaguar jawa jba-motors jeep jensen jetta jiangling-motors-corporation kaipan kaiser kamaz karlmann-king karma keating kenworth kia king-long koenigsegg ktm lada lagonda lamborghini lancia land-rover landwind laraki leapmotor lexus leyland li-auto lifan ligier lincoln lister lloyd lobini london-ev-company lordstown lotus lucid luxgen lynk-and-co mack mahindra man-truck-and-bus mansory marcos marlin maserati mastretta maxus maybach maz mazda mazzanti mclaren melkus mercedes-benz mercury merkur mills-extreme-vehicles morris-garages microcar mini mitsubishi mitsuoka mk-sportscars morgan morris mosler navistar national-electric-vehicle-sweden naza nio nikola nissan noble oldsmobile oltcit opel osca paccar packard pagini panhard panoz pars-khodro pegaso perodua peterbilt peugeot pgo pierce-arrow pininfarina plymouth polestar pontiac porsche praga premier prodrive proton puch qoros radical ram-trucks rambler ranz renault renault-samsung rezvani riley rimac rinspeed rivian robur roewe rolls-royce ronart rossion rover ruf saab saic-motor saipa saleen saturn scania scion seat setra shacman simca singer singulato sinotruk sisu skoda smart soueast spania-gta spirra spyker ssangyong ssc sterling studebaker stutz subaru suffolk suzuki talbot ata tatra tauro tavria techart temsa tesla thai-rung toyota tramontana trion triumph troller tucker tvr uaz ud-trucks ultima vandenbrink vauxhall vector vencer venturi venucia vinfast vlf-automotive volkswagen volvo wanderer w-motors wartburg weltmeister western-star westfield wiesmann wey willys-overland workhorse wuling xpeng yulon yutong zarooq-motors zastava zaz zeekr zenos zenvo zhongton zinoro zotye'''.split()

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


print('H A N G M A N   A U T O   B R A N D S')
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

