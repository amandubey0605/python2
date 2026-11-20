#Q8. Run pip freeze for the system interpreter. the contexts and create a similar 
#virtualenv

'''in terminal... like amansenv installing requirement.txt'''

#Q9.Explore the 'Flask'module and create a web server using flask and python.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(debug=True)

'''let's understand each message.
1. Your Flask code
from flask import Flaskapp = Flask(__name__)@app.route("/")def hello_world():    return "<p>Hello, World!</p>"app.run()



2. Understanding the terminal output
A. Development server warning
WARNING: This is a development server.
Do not use it in a production deployment.


This is a normal warning. Flask is telling you that its built-in server is intended for development and testing, not production.

B. Server started
Running on http://127.0.0.1:5000


Running successfully
- 127.0.0.1 means your local computer.
- 5000 is the default Flask port.
Open this address in your browser:
Open your Flask applicationYou should see:
Hello, World!
Your first Flask webpage

C. Successful request
"GET / HTTP/1.1" 200


200 means the browser successfully requested your homepage.

D. Favicon 404
"GET /favicon.ico HTTP/1.1" 404


This is not a serious error. Your browser automatically requests a favicon (the small website icon), but you haven't provided one.

You can ignore it for now.
3. What should you do next?
For local development, you can use:
app.run(debug=True)



This enables Flask's debugger and automatic reloading. Use it only for local development, never expose it in production.'''