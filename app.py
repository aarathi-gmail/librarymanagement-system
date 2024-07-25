from flask  import Flask,render_template,request,redirect,url_for,session
app=Flask(__name__)
app.secret_key='your_secret_key'
users={'admin':'password','user':'1234'}

@app.route('/')
def index():
   return 'welcome to login page'
@app.route('/login', methods={'GET','POST'})
def login():
    if request.method=='POST':
       username = request.form['username']
       password = request.form['password']
       if username in users and users[username] == password:
         session['username'] =  username
         return redirect(url_for('dashboard'))
       else:
         return render_template('login.html')
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
       return f'Hello,{session["username"]}!this is your dashboard'
    else:
       return redirect(url_for('login'))

@app.route('/logout')
def logout():
  session.pop('username',None)
  return redirect(url_for('index'))
if  __name__=='__main__':
    app.run(debug=True)



