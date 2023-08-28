working of POST method : data collected from form and displayed in the table.<br>
Note: Unlike the GET method, data is not shown in URL
<br><br>
<img src="https://github.com/alenscaria/Flask/assets/63664995/d2407ca2-b539-458d-b6f4-bdf54f5e1cbb" width=300>
<img src="https://github.com/alenscaria/Flask/assets/63664995/29a9c0a5-d999-45a2-a80b-72fba41d291b" width=300>
<br><br>
In the case of GET, <br>
name=request.args.get('name')
<br>
In the case of POST, <br>
name=request.form['name']
