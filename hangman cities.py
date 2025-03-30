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

words = '''kabul tirana algiers andorra-la-vella luanda saint-johns buenos-aires yerevan canberra vienna baku nassau manama dhaka bridgetown minsk brussels belmopan porto-novo thimphu sucre sarajevo gaborone brasilia bandar-seri-begawan sofia ouagadougou gitega phnom-penh yaounde ottawa praia bangui ndjamena santiago beijing bogota moroni kinshasa brazzaville san-jose yamoussoukro zagreb havana nicosia prague copenhagen djibouti roseau santo-domingo dili quito cairo san-salvador malabo asmara tallinn addis-ababa suva helsinki paris libreville banjul tbilisi berlin accra athens saint-george's guatemala-city conakry bissau georgetown port-au-prince tegucigalpa budapest reykjavik new-delhi jakarta tehran baghdad dublin jerusalem rome kingston tokyo amman astana nairobi tarawa pristina kuwait-city bishkek vientiane riga beirut maseru monrovia tripoli vaduz vilnius luxembourg skopje antananarivo lilongwe kuala-lumpur male bamako valletta majuro nouakchott port-louis mexico-city palikir chisinau monaco ulaanbaatar podgorica rabat maputo naypyidaw windhoek yaren kathmandu amsterdam wellington managua niamey abuja pyongyang oslo islamabad ngerulmud panama-city port-moresby asuncion lima manila warsaw lisbon doha muscat bucharest moscow kigali basseterre castries kingstown apia san-marino sao-tome riyadh dakar belgrade victoria freetown singapore bratislava ljubljana honiara mogadishu pretoria seoul juba madrid colombo khartoum paramaribo mbabane stockholm bern damascus taipei dushanbe dodoma bangkok lome nukualofa port-of-spain tunis ankara ashgabat funafuti kampala kyiv abu-dhabi london washington-dc montevideo tashkent port-vila vatican hanoi sanaa lusaka harare'''.split()

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


print('H A N G M A N   C I T I E S')
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
