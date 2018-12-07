# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""
def plcrep():
	from random import randint
	if randint(0,1)==1:
		return 'khartoum'
	else:
		return 'Atbra'
def perrep():
	from random import randint 
	if randint(0,1)==1:
		return 'Ali'
	else:
		return 'Omer'
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced = []
    # your code here
    test = ml_string.split()
    for i in test:
    	if word_in_pos(i,parts_of_speech)==None:
    		replaced.append(i)
    	else:
    		if word_in_pos(i,parts_of_speech)=='PLACE':
    			replaced.append(plcrep())
    		if word_in_pos(i,parts_of_speech)=='PERSON':
    			replaced.append(perrep())
    replaced = ' '.join(replaced)
    return replaced

print play_game(test_string, parts_of_speech)       

