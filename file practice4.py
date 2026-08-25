#A file contains a word "donkey" multiple times. you need to write a program which replace the word with ##### by updating the same file.
def overWrite():
    with open("overwriting.txt","r") as f:
        update=f.read()
        if "donkey" in update:
            print("Found!")
            update= update.replace("donkey","######")
            with open("overwriting.txt","w") as f:
                 f.write(update)
            
    return update
           
overWrite()                   
