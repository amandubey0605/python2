# chaptert 5 - Dictionary amd sets
# Q1.WAP to create a dictionary  of hindi words with values as their english translation provides user with an option  to look it up
Dict={
      "pani":"water",
      "aag":"fire",
      "namaste":"hello",
      "Insaan":"human" 

}

words=input("Entter the word:  ")
meaning=Dict.get(words)

if meaning:
    print("English meaning: ",meaning)
else:
    print("no meaning found..")  

    #   OR
dict2={
     "paisa":"money",
     "hawaa":" air",
     "bookh":"hunger",
     "kalam":"pen"

}    
word=input("Enter the word: ")
print(dict2[word])
