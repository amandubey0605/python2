# a spam comment is define as the text containing following keyword: "make a lot of money","buy now"," subscribe this", "click this" write the program to detect this spam use condiontional statement.
p1="make a lot of money"
p2="buy now"
p3=" subscribe this"
p4="click this"

messege=input("Enter your messege: ")

if(messege==p1 or messege==p2 or messege==p3 or messege==p4):
    print("Its a spam messege: ",messege)
else:
    print("Its not a spam: ",messege)
print("code over")