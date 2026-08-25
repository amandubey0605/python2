#Write a class train which has method to book a ticket,get status(no of seats) and get fare informationof
#train running under indian railways
''''class Train():
    Trains="Indian Railways"
    def __init__(self,name,seatNo,timeing,Desination):
        self.name=name
        self.seatNo=seatNo
        self.timeing=timeing
        self.Desitnation=Desination
    
    def Ticket(self):
        print("your ticket is booked") 
# name=input("enter your name: ")
# seatno=int(input("enter your seat number: "))
done= Train("aman",6,4,"banglore")
print(f'your details: {done.Trains},\nname: {done.name},\nseatNO:{done.seatNo},\ntiming:{done.timeing}PM,\nDestination:{done.Desitnation}') 
done.Ticket()'''


#   OR
#import random  # or "from random import chose".(aise lenge to random.chose likhne ka jarurat nhi hai normal choise(200,100)likh sakte hai)
import random
class Train():
    def __init__(self, train_No):
         self.train_No=train_No
    def book_ticket(self, from_city, to_city):
        print(f"your ticket is booked in train no: {self.train_No}\n from: {from_city} to: {to_city}")

    def get_status(self):
        print(f" Train no: {self.train_No} is running successfully")
    def get_fare(self, from_city, to_city):
        print(f"your ticket fare is: {random.randint(200,1000)}")

t=Train(420)
t.book_ticket("Banglore","Garhwa")
t.get_status()
t.get_fare("Banglore","Garhwa")


        