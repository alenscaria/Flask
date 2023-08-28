from flask import Flask,render_template, request #module and class
app=Flask(__name__) #any name

#app routing - mapping specific url with asso. func
#<name> <int:age> <float:num1> print values in f'{age}'

@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    name=request.form['name']
    number=request.form['number']
    email=request.form['email']
    return render_template('register.html',name=name,number=number,email=email)


@app.route('/about')
def about():
    return "This is About Page"

@app.route('/product')
def product():
    return "Product Page"

@app.route('/product/laptop')
def laptop():
    return "Laptop Page"

#app.add_url_rule('/home','home',home)  #route,endpoint,func


if __name__=='__main__':
    app.run(debug=True)
