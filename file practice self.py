#  replace the word with the help of function in a list
def repl():
    print("replacing.....")  
    with open("file list.txt","r") as f:
      text=f.read()
      
      if "donkey" in text or "Donkey" in text or "DONKEY" in text:
          print("Found!")
          text=text.replace("donkey","######").replace("DONKEY","######").replace("Donkey","######")

          with open("file list.txt","w") as f:
            f.write(text)

    return text
repl()   

#      OR
# import re     #re.IGNOREcase  means python ignores uppercase/lowercase differences.

# def repl():
#     print("Replacing.....")

#     with open("file list.txt", "r") as f:
#         text = f.read()

#     # Replace donkey in any combination of uppercase/lowercase
#     new_text = re.sub("donkey", "######", text, flags=re.IGNORECASE)

#     if new_text != text:
#         print("Found!")

#         with open("file list.txt", "w") as f:
            # f.write(new_text)

    # return new_text


# repl()
