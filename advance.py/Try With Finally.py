'''
Python offers a "finally" clause which ensures execution of a piece of code
inspective of the exception.
'''
def main():
  try:  #first it try if it run or not (sahi hoga to print hoga nhi to exception print hoga)
      a=int(input("enter the number: "))
      print(a)
      return

  except Exception as e:
       print(e) 
       return 

  finally:    # ye runhoga hi hoga chahe try success ho ya except
     print("I am inside finally") #it is the piece of code

main()     
'''ham finnally ke jagah bss print ("i am inside finally") v likh sakte hai
 wo same wahi krega finally ki tarah .
 but finally function m use hota hai jab ham function call krenge
 suppose apne try ke baad return kr diya to apka print nhi chalega
 '''