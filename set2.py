# Q2.Can we have a set with  18(int) and '18'string as a value in it

s=set()
s.add(18)
s.add("18")
print("sets: ",s)
print("type of 18: ",type(18))
print("type of '18': ",type("18"))

# Q3 what is the length of the following set
# s=set()
# s.add(20)
# s.add(20.0)
# s.add('20')
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print("sets: ",s)
print(f'the length of set is:{len(s)}')