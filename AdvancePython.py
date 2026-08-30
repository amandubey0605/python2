#NEWLY ADDED FEATURES IN PYTHON
'''Like- WALRUS OPERATOR
  the walrus operator(:=) allows you to assign values to variables as part of an 
  Expression. this operator named for its resembalance(similarity) to the eyes and 
  tusk(long) of a walrus ,is officially called the assignment expression.
  
  SYNTEX-
  if(n:= len([1,2,3,4,5])) >3:
     print(f'list is too long ({n} elements, expected <= 3)')

  output: List is too long(5 elements, expected <=3)   
  '''


'''TYPE DEFINITIONS IN PYTHON
type hints are added using the colon(:) 
syntax for the variables and the -> syntax for function return types:
 
 age: int =25
 
 # function type hints     (kon sa function kya return kr rha hai kis type ka value return
                            kr rha hai aur kon sa function kis type ka values or kon sa variable parameter
                              pass ho rha hai unke types kya hai  )
   def sum(a: int , b:int) -> int:
        return a+b  
            '''


''' ADVANCED TYPE HINTS

PYTHON's typing modules provides more advanced type hints,such as List, Tuple, Dict and union

we can import list, tuple ,dict, union type from typing modules like this:

"from typing import list,tuple,dict,union"'''