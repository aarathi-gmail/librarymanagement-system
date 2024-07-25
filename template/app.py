from flask import Flask,render_template,request ,redirect,url _app=Flask(_name_)
books=[]
#routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book',methods=['GET','POST'])
def add_book():
    ifr equest.method=='POST':
        title=request.form['title']
   author=request.form['author']
   books.append({'title': title,'author':author})
   return redirect(url_for('index'))
   return render_template('add_book.html')

if __name__=='__main__':
    app.run(debug=True)