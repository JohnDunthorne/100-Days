# hangman
import random
import os

def print_centered(message, width=80):
    print(message.center(width))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()
print_centered('''
                  Welcome to:
 __ __   ____  ____    ____  ___ ___   ____  ____  
|  |  | /    ||    \  /    ||   |   | /    ||    \ 
|  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
|  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
|  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
|  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
|__|__||__|__||__|__||___,_||___|___||__|__||__|__|
      
              Press Enter to play
      
''')
input("")
clear_terminal()
word_list = [
    "abacus", "abbreviate", "aberration", "abhorrence", "abomination", "abstinence", "accelerate", "accentuate", 
    "accommodate", "accompaniment", "acquisition", "adulteration", "adventurous", "aesthetic", "affiliation", 
    "aggrandize", "alleviate", "amalgamation", "ambiguous", "ameliorate", "anachronism", "analogous", 
    "anathematize", "annihilation", "antagonistic", "apocalyptic", "apprehensive", "archaeology", "articulate", 
    "ascertain", "assimilate", "astronomical", "atmosphere", "attenuate", "authenticity", "benevolent", 
    "biotechnology", "bureaucracy", "cacophony", "camouflage", "capitulate", "celestial", "circumference", 
    "coalesce", "cognizant", "collaboration", "commemorate", "concatenate", "conflagration", "conglomerate", 
    "conscientious", "consequential", "contradiction", "corroborate", "cryptocurrency", "decipher", "delectable", 
    "denunciation", "deprecate", "derogatory", "determination", "discombobulate", "disparate", "eccentricity", 
    "effervescent", "egalitarian", "electromagnetic", "embellish", "enervate", "enthusiastic", "ephemeral", 
    "equivocate", "esoteric", "evanescent", "exacerbate", "exemplify", "expedite", "extrapolate", "facetious", 
    "fastidious", "felicitous", "flabbergasted", "fluctuate", "fortuitous", "frustration", "garrulous", 
    "genealogy", "gesticulate", "gratuitous", "gregarious", "haphazard", "harangue", "hierarchy", "homogeneous", 
    "idiosyncrasy", "ignominious", "illustrious", "immutable", "impetuous", "implacable", "impromptu", "incongruous", 
    "indeterminate", "indispensable", "indomitable", "inexorable", "inquisitive", "insidious", "intrepid", 
    "intransigent", "intrepid", "introspective", "irrefutable", "juxtapose", "kaleidoscope", "labyrinthine", 
    "lamentation", "lexicon", "libertarian", "ludicrous", "magnanimous", "malicious", "manifestation", "mellifluous", 
    "mercurial", "metamorphosis", "meticulous", "misanthrope", "monotonous", "multifarious", "nefarious", 
    "obfuscate", "oblivion", "omnipotent", "omniscient", "onus", "opulent", "ostentatious", "paradoxical", 
    "penultimate", "perfidious", "perfunctory", "perspicacious", "petrify", "philanthropy", "platitude", 
    "plethora", "pontificate", "pragmatic", "precipitous", "procrastinate", "profligate", "proliferate", 
    "propinquity", "quandary", "querulous", "quixotic", "rampant", "recalcitrant", "reciprocal", "reconciliation", 
    "recumbentibus", "refrigerator", "rejuvenate", "reminisce", "repertoire", "repudiate", "resilient", 
    "resplendent", "reticent", "rhetorical", "sacrosanct", "sagacious", "salubrious", "sanguine", "sardonic", 
    "saturnine", "serendipity", "serendipity", "sibilant", "soliloquy", "somnambulist", "spurious", "stoicism", 
    "sycophant", "symbiotic", "taciturn", "tempestuous", "tenacious", "ubiquitous", "umbrage", "unprecedented", 
    "usurp", "vacillate", "vagabond", "vehement", "verisimilitude", "verbose", "vexatious", "vicarious", 
    "vindicate", "virulent", "voracious", "wanderlust", "xenophobia", "yesteryear", "zealous", "zeitgeist"
]
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
ENDC = '\033[0m'
chosen_word = random.choice(word_list)
display = "_" * (len(chosen_word))
print(f"Your word is this long: ", end="")
print(BLUE + ' '.join(display) + ENDC)
numberoflives = 6
incorrectlyguessedletters = ""
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(f"{stages[numberoflives]}")
while numberoflives > 0:

    while "_" in display:
        guess = input("Guess a letter: ").lower()
        clear_terminal()
        newdisplay = ""
        correctguess = False
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                newdisplay += guess
                correctguess = True
            else:
                newdisplay += display[i]

        display = newdisplay

        if not correctguess:
            if guess not in incorrectlyguessedletters:
                incorrectlyguessedletters += guess
                numberoflives -= 1
            else:
                print(RED + f"you've already tried {guess}" + ENDC)
            
        if numberoflives <= 0:
            break
        print("")
        print(f"your word so far: ", end ="")
        print(BLUE + ' '.join(display) + ENDC)
        print(f"{stages[numberoflives]}")
        print(f"Letters you've tried already: ", end ="")
        print(YELLOW + ' '.join(incorrectlyguessedletters) + ENDC)
        print("")
    if display == chosen_word:
        print(GREEN + "Congratulations! You guessed the word:", chosen_word + ENDC)
        break
    else:
        print(RED + f"Sorry you ran out of tries the word was {chosen_word}" + ENDC)
        print(f"{stages[numberoflives]}")
        break