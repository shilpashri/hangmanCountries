import random

name = raw_input("What is your name? ")
print "Hello, " + name, ", Time to play hangman!"
print "Start guessing, alphabet by alphabet..."

countries = ["india", "france", "ireland", "germany", "italy", "austria", "belgium", "canada", "hungary", "chile", "sweden", "switzerland", "united states", "united kingdom", "greece", "denmark", "iceland", "japan", "portugal", "new zealand", "norway"]
word = random.choice(countries);
guesses = ''
turns = 10

while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print char,
        else:
            print "_",
            failed += 1    
    if failed == 0:        
        print "You won, " + name
        break              
    guess = raw_input("guess a character:") 
    guess = guess.lower()
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print "Wrong! You have", + turns, 'more guesses' 
        if turns == 0:           
            print "You Lost, the word was " + word  