#incorrect answer
#lives
import random
import string
import os
from hangman_visual import lives_visual_dict

def hidden_word(word, user):
    result = True
    for char in word:
        if char == '-' or char == ' ':
            print(f' {char} ', end="")
        if char in user:
            print(f' {char} ', end="")
        elif char.isalpha():
            print(' _ ', end="")
            result = False
    print("\n")

    return result

 
def available_letter(user):
    print(f"You have used: {user}")
        
def get_random_word():
    easy = ['creak', 'lapse', 'eddic', 'tidde', 'muser',                                                           # Words for game
         'chief', 'swelt', 'viage', 'topic', 'scots',
          'fairy', 'gator', 'glass', 'kneel', 'laces',
          'copps', 'paste', 'narre', 'brail', 'beeld',
          'ankle', 'apple', 'birds', 'aunts', 'blood',
         'bones', 'forty', 'glitz', 'gnome', 'goats',
          'fairy', 'gator', 'glass', 'kneel', 'laces',
          'patio', 'party', 'taffy', 'zones', 'wages']

    medium = ['bewailable', 'sismometer', 'emendicate', 'alcoranist', 'millesimal',
        'restitutor', 'derogation', 'implicitly', 'repellency', 'aggravated',
        'understand', 'amblygonal', 'courageous', 'overlaying', 'cultivated',
        'shadowless', 'episternum', 'triflorous', 'tobogganer', 'antimonial',
        'jackrabbit', 'maximizers', 'abnormally', 'abolishers', 'adrenaline',
        'california', 'basketball', 'friendship', 'renovation', 'skateboard',
        'understand', 'leadership', 'restaurant', 'generation', 'girlfriend',
        'vegetables', 'protection', 'trampoline', 'rainforest', 'instrument']

    hard = ['compunctionless', 'indubitableness', 'holocrystalline', 'sulphophosphite',
             'logarithmetical', 'supradecompound', 'spermatophorous', 'comfortableness',
            'metallographist', 'instrumentation', 'parthenogenesis', 'inalienableness',
            'maneuverability', 'persulphocyanic', 'excommunication', 'acclimatization',
             'rationalisation', 'mischievousness', 'kindheartedness', 'procrastinating',
            'confidentiality', 'instrumentation', 'inaccessibility', 'marginalization']
    true = True
    while true:
        choice = input("Choose difficulty: \nEASY(e)\nMEDIUM(m)\nHARD(h)\n")
        if choice == 'e':
            words = random.choice(easy)
            break
        elif choice == 'm':
            words = random.choice(medium)
            break
        elif choice == 'h':
            words = random.choice(hard)
            break
        else:
            true = False
    else:
        print("Your answer is inccorect")
        get_random_word()

    return words


def game(): 
    lives = 7
    word = get_random_word()
    user = list()
    alphabet = list(string.ascii_lowercase)
    
    while lives > 0:
        print(f"Your word is:")
        print(lives_visual_dict[lives])
        symbols = hidden_word(word, user)
        if symbols:
            print("YOU WON")
            break

        available_letter(user)
        
        letter_input = input('\nGuess the letter:\n').lower()
        
        if letter_input.isalpha == False:
            print("try to use another one")
            continue
        
        if letter_input in user:
            print("try to use another one")
            continue
        
        user.append(letter_input)
        print(user)
        word_letters = set(word)
        if user == word_letters:
            print(f"You have {lives} lives.")
        else:
            lives -= 1
            print(f"You have {lives} lives.")
            continue
        
        
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"You r looser!\nThe word was {word}")
game()
            
