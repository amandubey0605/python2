#can you change the self-parameter inside a class to something else (say "aman").try chanding self to  "slf" or "aman"
#and see the effects (no effect occur if we change self with any letter the any whre we writen self replace with that letter 
#no error found)
#Example
import random
class Train():
    def __init__(sel, train_No):
         sel.train_No=train_No
    def book_ticket(sel, from_city, to_city):
        print(f"your ticket is booked in train no: {sel.train_No}\n from: {from_city} to: {to_city}")

    def get_status(sel):
        print(f" Train no: {sel.train_No} is running successfully")
    def get_fare(sel, from_city, to_city):
        print(f"your ticket fare is: {random.randint(200,1000)}")

t=Train(420)
t.book_ticket("Banglore","Garhwa")
t.get_status()
t.get_fare("Banglore","Garhwa")

#no any change occurs