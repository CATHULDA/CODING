#------------------------------------------------------------------------------------------

import random
import csv

print("""

--------------------------------------------------------------------------

#####   #   ####   ###  #####    ####  #####   #   ###   ##### ##  # #####
  #    # #  #   # #   #   #      #   # #      # #  #  #    #   # # # #
  #    # #  ####  #   #   #      ##### #####  # #  #   #   #   # # # # ###
  #   ##### #  #  #   #   #      #  #  #     ##### #  #    #   # # # #   #
  #   #   # #   #  ###    #      #   # ##### #   # ###   ##### #  ## #####

--------------------------------------------------------------------------

""")

rnd_group = random.randint(1,5)
rnd_reverse = random.randint(0,1)

print("What is your name?:")
name = input()

      
#------------------------------------------------------------------------------------------

major_arcana = {"The Fool": 0, "The Magician": 1, "The High Priestess": 2, "The Empress": 3, "The Emperor": 4,
                "The Hierophant": 5, "The Lovers": 6, "The Chariot": 7, "Strength": 8, "The Hermit": 9,
                "Wheel of Fortune": 10, "Justice": 11, "The Hanged Man": 12, "Death": 13, "Temperance": 14,
                "The Devil": 15, "The Tower": 16, "The Star": 17, "The Moon": 18, "The Sun": 19, "Judgement": 20,
                "The World": 21}

the_wands = {"Ace of Wands": 0, "Two of Wands": 1, "Three of Wands": 2, "Four of Wands": 3, "Five of Wands": 4,
             "Six of Wands": 5, "Seven of Wands": 6, "Eight of Wands": 7, "Nine of Wands": 8, "Ten of Wands": 9,
             "Page of Wands": 10, "Knight of Wands": 11, "Queen of Wands": 12, "King of Wands": 13}

the_cups = {"Ace of Cups": 0, "Two of Cups": 1, "Three of Cups": 2, "Four of Cups": 3, "Five of Cups": 4,
             "Six of Cups": 5, "Seven of Cups": 6, "Eight of Cups": 7, "Nine of Cups": 8, "Ten of Cups": 9,
             "Page of Cups": 10, "Knight of Cups": 11, "Queen of Cups": 12, "King of Cups": 13}

the_swords = {"Ace of Swords": 0, "Two of Swords": 1, "Three of Swords": 2, "Four of Swords": 3, "Five of Swords": 4,
             "Six of Swords": 5, "Seven of Swords": 6, "Eight of Swords": 7, "Nine of Swords": 8, "Ten of Swords": 9,
             "Page of Swords": 10, "Knight of Swords": 11, "Queen of Swords": 12, "King of Swords": 13}

the_pentacles = {"Ace of Pentacles": 0, "Two of Pentacles": 1, "Three of Pentacles": 2, "Four of Pentacles": 3, "Five of Pentacles": 4,
             "Six of Pentacles": 5, "Seven of Pentacles": 6, "Eight of Pentacles": 7, "Nine of v": 8, "Ten of Pentacles": 9,
             "Page of Pentacles": 10, "Knight of Pentacles": 11, "Queen of Pentacles": 12, "King of Pentacles": 13} 

#------------------------------------------------------------------------------------------

def card_output(text_file):
    with open(text_file) as tarot_file:
        tr_dict = csv.DictReader(tarot_file)
        count = 0
        up_to = (rnd_card * 2) + rnd_reverse
        print(name + " here is your tarot card of the day:")
        for row in tr_dict:
            if count == up_to:
                print(row['Definition'])
            count += 1

#------------------------------------------------------------------------------------------

if rnd_group == 1:
    rnd_card = random.randint(0,21)
    ma_keys = list(major_arcana.keys())
    chosen_ma = ma_keys[rnd_card]
    card_output("major_arcana.csv")
        
elif rnd_group == 2:
    rnd_card = random.randint(0,13)
    tw_keys = list(the_wands.keys())
    chosen_tw = tw_keys[rnd_card]
    card_output("the_wands.csv")
    
elif rnd_group == 3:
    rnd_card = random.randint(0,13)
    tc_keys = list(the_cups.keys())
    chosen_tc = tc_keys[rnd_card]
    card_output("the_cups.csv")
    
elif rnd_group == 4:
    rnd_card = random.randint(0,13)
    ts_keys = list(the_swords.keys())
    chosen_ts = ts_keys[rnd_card]
    card_output("the_swords.csv")
        
else:
    rnd_card = random.randint(0,13)
    tp_keys = list(the_pentacles.keys())
    chosen_tp = tp_keys[rnd_card]
    card_output("the_pentacles.csv")

#------------------------------------------------------------------------------------------

        








