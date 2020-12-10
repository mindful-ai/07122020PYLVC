import json

def jumble(word):
    return word

# Welcome message
print("-"*80)
print("\t\t\tWELCOME TO THE WORD JUMBLE GAME")
print("\t\tTry to guess the jumbled word shown on the screen")
print("-"*80)

# Load the data

with open('words.json') as f:
  data = json.load(f)

print(data)

score = 0
# Repeat for all words
for word in data:

    # Pick a word
    # Jumble the word
    jword = jumble(word)

    # Show the word
    print("The word is -------> ", jword)

    # Get the user input - attempt #1
    uword = input("? ")

    # if it failes - show clue 
    if(uword == word):
        score += 1
        continue
    else:
        print("Not correct")
        print("Clue -> ", data[word])
        # Get the user input - attempt #2
        uword = input("? ")
        # Compare
        if(uword == word):
            # update score
            score += 1
        else:
            print("Not correct -> Moving on...")


# Show the score
print("-"*80)
print("SCORE :", score)