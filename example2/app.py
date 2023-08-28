from flask import Flask,render_template, request #module and class
app=Flask(__name__) #any name

#app routing - mapping specific url with asso. func
#<name> <int:age> <float:num1> print values in f'{age}'

@app.route('/') 
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':

        if request.form['name']=='user' and request.form['password']=='user123':
            return render_template('dashboard.html')
        else:
            error="wrong username or password"
            return render_template('login.html',error=error)
    else:
        return render_template('login.html')

#app.add_url_rule('/home','home',home)  #route,endpoint,func


if __name__=='__main__':
    app.run(debug=True)

