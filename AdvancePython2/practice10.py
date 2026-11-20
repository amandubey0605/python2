'''Task: Create three webpages using Flask.
1. / → Display Welcome to My Website
2. /about → Display This is my About Page
3. /contact → Display Contact Me
Hint: You can use @app.route() multiple times.

Example:
@app.route("/about")
def about():   
    return "This is my About Page"

Write the remaining routes yourself and send me your code. I'll check it like your Python mentor. 💪'''


from flask import Flask

app = Flask(__name__)

@app.route("/")
def display():
    return "<p>Welcome to My Website!</p>"

@app.route("/about")
def about():
    return "<p>This is my About Page</p>"

@app.route("/contact")
def contact():
    return "<p>Contact Me!</p>"

app.run(debug=True)


'''Step 1: Check the About page
Look at the address bar at the top of your VS Code browser. Currently, it shows:
http://127.0.0.1:5000/


Click the address bar, remove the last / if you want, and type:
http://127.0.0.1:5000/about


Press Enter.

You should see:
This is my About Page
Step 2: Check the Contact page
Again, click the address bar and type:
http://127.0.0.1:5000/contact


Press Enter.

You should see:
Contact Me!
Understand how it works
URL	Flask function	Output
/	   display()	    Welcome to My Website!
/about	 about()	This is my About Page
/contact  contact()	 Contact Me!

Remember: @app.route() connects a URL to a Python function. When someone visits that URL, Flask runs the corresponding function.
'''