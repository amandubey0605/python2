# WAP to read the text from a given file'poems.txt' and find out wheather it contins
# the word 'twinkle'
with open("poem.txt","r") as f:
   data= f.read()
   
   if("Twinkle" in data):
       print("Twinkle is present in the file")
       print(f'The number of Twinkle in the file is:{data.lower().count("twinkle")}')
   else:
        print("Twinkle is not in the file")
        