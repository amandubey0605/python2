# IF __NAME__ =='__MAIN__'
'''__name__  evaluates to the name of the modules in python from where the program
is ran.

if the modules is being run directly from the commond line,
the '__name__' is set to string "__main__".thus,this behaviour is used
to check whether the modules is run run directly or imported to another file.
'''
 


def myFunc():
    print("hello!")

#myFunc()
#print(__name__)  

'''in print(__name__) it give __main__ as output  kyu ki mai ne module ke iss code ko
module wale file se hi run kiya hai lakin agar main main.py me run kruu to ye my_module return krega
'''  

'''agar apne module ko direcly call kiya tabhi ye code execute hoga
agar main.py me run krana hoga to "if __name__== "my_module hoga" jis file se import krna
hai uska namehoga'''
if __name__ =="__main__": 
    #if the code is directly executed by running the file its present in!
    print("We are directly running this code ")
    myFunc()
    print(__name__)






'''when importing it.

We only want to use its functions.

For example:

📄 calculator.py
def add(a, b):
    return a + b


print(add(5, 10))
📄 main.py
import calculator

answer = calculator.add(100, 50)

print(answer)

When you run main.py, the output will be:

15
150

Why did 15 print? 🤔

Because Python imported calculator.py, and while importing, it ran:

print(add(5, 10))
Step 3: Now use __name__ == "__main__" 🔥

Change calculator.py to:

def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(5, 10))

Now run:

📄 main.py
import calculator

answer = calculator.add(100, 50)

print(answer)

Output:

150

🎉 The 15 does not print anymore.

Why? 🧠

When you run:

python calculator.py

Python gives:

__name__ = "__main__"

So:

if __name__ == "__main__":

is True ✅

The code inside runs.

But when you do:

import calculator

Python gives the imported file:

__name__ = "calculator"

So:

if __name__ == "__main__":

is False ❌

The code inside does not run.

Remember this simple rule ⭐
What you do	__name__
Run the file directly	"__main__"
Import the file	File name
In one sentence:

if __name__ == "__main__": means: Run this code only when this file is run directly, not when another Python file imports it.

The best experiment for you now 👨‍💻

Make these two files yourself:

calculator.py → contains the add() function and the if __name__ == "__main__" block.

main.py → imports calculator and uses calculator.add().'''