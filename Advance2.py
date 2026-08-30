from typing import List,Tuple,Dict,Union

#list of integers
numbers: List[int]=[1,2,3,4,5]

#Tuple of a string and an integer
person: Tuple[str , int] = ("Alice",30)

#Dictionary with string keys and integer values
scores: Dict[str,int]= {"Alice": 90, "Bob":85}

#Union type for Variables that can hold multiple types
identifier: Union[int,str]="ID123"
identifier =1234 #also valid 
 
'''these annotations helps in making the code self-documenting and allow developer to 
understand the data structure used at glance (look at something quickly or briefly.)'''