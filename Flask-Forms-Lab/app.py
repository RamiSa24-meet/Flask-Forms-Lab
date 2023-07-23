from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'super-secret-key'

info = {'llo2ay':'123' , "rami":"samra","lol":"dope", }

facebook_friends = ["bashar hussein","tamer yaqub","majd trabeh", "Eid Samra", "mary samra ", "bseeil "]


@app.route('/home')  # '/' for the default page
def home():
  return render_template('home.html',friends= facebook_friends)




@app.route('/friend_exists/<string:name>')  # '/' for the default page
def friend_exists(name):
  return render_template('friend_exists.html',n =name,friend_exists = facebook_friends)



@app.route('/',methods=['GET', 'POST'])  # '/' for the default page
def login():
  if request.method == 'GET':
    return render_template('login.html')
  else:
    z =request.form['username'] 
    x = request.form['password']
    if (z in info and x ==a info[z])and (len(x)>7 and len(z)>7):
      return redirect(url_for('home'))
    else:
      print("hello")
      return render_template('login.html')
    
	      




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)