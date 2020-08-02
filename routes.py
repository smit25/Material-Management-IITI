from flask import Flask ,render_template,flash,redirect,request,url_for
import mysql.connector
# from datetime import datetime

try:
	print("connected")
	connection = mysql.connector.connect(user='root', password='Password@123', host='localhost', database='data')
	print("connected")

	cur = connection.cursor(buffered=True)
	print("connected")
except:
	print("not connected")
	
app = Flask(__name__,template_folder='template')
#for home page

@app.route('/' ,methods=['GET','POST'])
def home():
	if request.method=='POST':
		if 'INDENT' in request.form:
			return redirect(url_for('indentcategory'))
		if 'cred' in request.form:
			return redirect(url_for('login'))
	else:
		return render_template('home.html')

#for loginpage
@app.route('/Login',methods=['GET','POST'])

def login():
	# base()
	if request.method == 'POST':
		if 'sign' in request.form:
			if request.form['sign'] == 'signin':
				return redirect(url_for('signin'))
			if request.form['sign'] == 'signup':
				return redirect(url_for('signup'))
		else:
			return base()
	else:
		return render_template('login.html', title = 'Login')

login =0
# FOR SIGNIN
@app.route('/login/signin', methods = ['GET','POST'])
def signin():
	# base(request)
	if request.method == 'POST':
		if 'signin' in request.form:
			User = request.form
			email = User['username']
			Password = User['password']
			# cur=mysql.connection.cursor()
			s_user=cur.execute("SELECT username from employee as u where u.username = '"+email+"';")
			s_user =cur.fetchall()
			if s_user == '' :
				print("Either sign up or enter the correct id")
				return redirect(url_for('signin'))
			if s_user == 'Admin' :
				s_pass=cur.execute("SELECT password from employee as u where u.username = '"+email+"';")
				s_pass = cur.fetchall()
				print(Password,s_pass)
				if s_pass[0][0] == Password:
					print("Login Successful As Admin")
					return redirect(url_for('Admin'))
			else:
				s_pass=cur.execute("SELECT password from employee as u where u.username = '"+email+"';")
				s_pass = cur.fetchall()
				print(Password,s_pass)
				if s_pass[0][0] == Password:
					print("Login Successful As employee")
					return redirect(url_for('employee'))
				else:
					print("Enter the correct password!")
					return redirect(url_for('signin'))
		else:
			return base()
		# cur.close()
	else:
		return render_template('signin.html', title = 'Sign-in')


# FOR SIGNUP
@app.route('/login/signup', methods = ['GET','POST'])
def signup():
	
	login=1
	if request.method == 'POST':
		if 'signup' in request.form:

			User= request.form
			f_name=User(f_name)
			password=User(password)
			print("hey")
		# cur=mysql.connection.cursor()
			cur.execute("INSERT INTO employee(username,password) VALUES ('"+f_name+"','"+password+"');")
			connection.commit()
		# cur.close()
			print("Thank you")

			return redirect(url_for('employee.html', username=username))
		else:
			return base()
	else:
		return render_template('signup.html', title ='Sign-Up')
@app.route('/indentcategory', methods=['GET','POST'])
def indentcategory():
	if request.method=='POST':
		if 'DIRECT PURCHASE' in request.form:
			return redirect(url_for("directpurchase"))
		elif 'LOCAL PURCHASE >25000' in request.form:
			return redirect(url_for("localpurchase"))
		elif 'GEM' in request.form:
			return redirect(url_for("GEM"))
	else:
		return render_template('indentcategory.html')

@app.route('/indentdirect', methods=['GET','POST'])
def directpurchase():
	if request.method == 'POST':
		I=request.form
		indent_date=I['indentdate']
		Dept=I['Dept']
		Name=I['Name']
		Desgn=I['Desgn']
		IAA=I['IAA']
		Radio=I['budgetT']
		cost=I['cost']
		PFby=I['PFby']
		itemname=I['itemname']
		subcat=I['subcat']
		brand=I['brand']
		qty=I['quantity']
		warrenty=I['warrenty_period']
		expectdate=I['expecteddate']
		print(Radio)
		cur.execute("INSERT INTO indentor(indent_date,handlename,Designation,indent_approving,Budget_type,       estimated_cost,expected_delivery_period) VALUES ('"+indent_date+"','"+Name+"','"+Desgn+"','"+IAA+"','"+Radio+"','"+cost+"','"+expectdate+"');")
		cur.execute("INSERT INTO main_cat(item_name,brand,quantity,warrenty_period) VALUES ('"+itemname+"','"+brand+"','"+qty+"','"+warrenty+"');")
		cur.execute("INSERT INTO sub_cat(item_specification) VALUES ('"+subcat+"');")
		connection.commit()
		return redirect(url_for(''))
	else:
		return render_template("indentdirect.html")

@app.route('/indentlocal', methods=['GET','POST'])
def localpurchase():
	return render_template("indent.html")

@app.route('/indentgem', methods=['GET','POST'])
def GEM():
	return render_template("indent.html")

@app.route('/Admin', methods=['GET','POST'])
def Admin():
	if request.method=='POST':
		S=request.form
		if 'DIRECT PURCHASE' in S:
			return redirect(url_for('admin_directpurchase'))
		if 'LOCAL PURCHASE >25000' in S:
			return redirect(url_for('admin_localpurchase'))
		if 'GEM' in S:
			return redirect(url_for('admin_gem'))
	else:
		return render_template("Admin.html",form=form)

@app.route('/admin_directpurchase', methods=['GET','POST'])
def admin_directpurchase() :
	if request.method=='POST':
		cur.execute("SELECT * from indentor;")
		forms=cur.fetchall()	



   return redirect(url_for('placeorder_directpurchase'))
   
   else:
   	return render_template("admin_directpurchase.html") # will show all tables with respective appove buttons and placeorder buttons



@app.route('/admin_localpurchase', methods=['GET','POST'])
def admin_localpurchase() :
    if request.method=='POST':
		forms=cur.execute("SELECT * from indentor;") #only in this particular category forms should get dispalyed
		forms=cur.fetchall()
		return redirect(url_for('placeorder_localpurchase'))
   
   else:
   	return render_template("admin_localpurchase.html") # will show all tables with respective placeorder buttons






@app.route('/admin_gem', methods=['GET','POST'])
def admin_gem() :
    if request.method=='POST':
		forms=cur.execute("SELECT * from indentor;")
		forms=cur.fetchall()

        return redirect(url_for('placeorder_gem'))
   
   else:
   	return render_template("admin_gem.html") # will show all tables with respective appove buttons and placeorder buttons

@app.route('/placeorder_directpurchase', methods=['GET','POST'])
def placeorder_directpurchase():
	if request.method=='POST':
		
    




     return render_template("placeorder_directpurchase.html")






@app.route('/placeorder_localpurchase', methods=['GET','POST'])
def placeorder_localpurchase():
      



	return render_template("placeorder_localpurchase.html")






@app.route('/placeorder_gem', methods=['GET','POST'])
def placeorder_gem():



	return render_template("placeorder_gem.html")






if __name__ == '__main__':
	app.run(debug=True)
