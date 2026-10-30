'''pip freeze or python -m pip freeze, returns all the package installed in a given python enviornment
along with the versions.'''

'''AND 

pip freeze > requirements.txt (the given command creates the file named 'requirements.txt
'in the same dictionary containing the output of 'pip freeze')
 we can disstributes this file to other user, and they can recreate the same environment
 using:  pip install -r requirements.txt OR python -m pip install -r requirements.txt'''
