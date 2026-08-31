#dictionary merge and update operators
'''New operators "|" and "|=" allow for merging and updating dictionaries.
Sytex- '''

dict1={'a':1,'b':2}
dict2={'b':3,'c':4}

merged = dict1 | dict2
print(merged,end=" ")

'''we can now use multiple context managers in a single "with" statement more cleanly
using the parenthesised context manager'''
with (
    open('file.txt') as f1,
    open('file3.txt') as f2
):
    data1 = f1.read()
    data2 = f2.read()

    print(data1)
    print(data2)
    

