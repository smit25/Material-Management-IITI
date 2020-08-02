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
f_id = 0
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
		return render_template('login.html') #title = 'Login')

login =0
# FOR SIGNIN
@app.route('/login/signin', methods = ['GET','POST'])
def signin():
	# base(request)
	if request.method == 'POST':
		if 'signin' in request.form:
			User = request.form
			email = User['email']
			Password = User['password']
			# cur=mysql.connection.cursor()
			s_user=cur.execute("SELECT username from employee as u where u.username = '"+email+"';")
			s_user =cur.fetchall()
			if s_user == '' :
				print("Either sign up or enter the correct id")
				return redirect(url_for('signin'))
			if s_user[0][0] == 'Admin' :
				s_pass=cur.execute("SELECT password from employee as u where u.username = '"+email+"';")
				s_pass = cur.fetchall()
				print(s_pass[0])
				print(Password,s_pass[0][0])
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
		# cur.close()
	else:
		return render_template('signin.html', title = 'Sign-in')


# FOR SIGNUP
@app.route('/login/signup', methods = ['GET','POST'])
def signup():
	
	login=1
	if request.method == 'POST':
		if 'signup' in request.form:
			User = request.form
			email = User['email']
			Password = User['password']
		# cur=mysql.connection.cursor()
			cur.execute("INSERT INTO employee(username,password) VALUES ('"+email+"','"+Password+"');")
			connection.commit()
		# cur.close()
			print("Thank you")
		return redirect(url_for('employee'))
	else:
		return render_template('signup.html', title ='Sign-Up')


@app.route('/employee',methods=['GET','POST'])
def employee():
	print("employee")
	if request.method=='POST':
		if 'OK' in request.form:
			return redirect(url_for('login'))
	else:
		return render_template('employee.html')

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
		vendor_n=I['vendorname']
		print(vendor_n)

		cur.execute("INSERT INTO indentor(indent_date,handlename,Designation,indent_approving,Budget_type, estimated_cost,expected_delivery_period) VALUES ('"+indent_date+"','"+Name+"','"+Desgn+"','"+IAA+"','"+Radio+"','"+cost+"','"+expectdate+"');")
		connection.commit()
		cur.execute("SELECT max(indent_id) from indentor")
		indent_id=cur.fetchall()
		print(indent_id[0][0])
		cur.execute("INSERT INTO main_cat(item_name,brand,quantity,warrenty_period) VALUES ('"+itemname+"','"+brand+"','"+qty+"','"+warrenty+"');")
		connection.commit()
		cur.execute("INSERT INTO sub_cat(item_specification) VALUES ('"+subcat+"');")
		connection.commit()
		cur.execute("INSERT INTO vendor(vendor_name, indent_id) VALUES ('"+vendor_n+"',"+str(indent_id[0][0])+");")
		connection.commit()
		cur.execute("INSERT INTO purchase_types(indent_id,direct_purchase) VALUES("+str(indent_id[0][0])+",'directpurchase');")
		connection.commit()
		return redirect(url_for('message'))
	else:
		return render_template("indentdirect.html")

@app.route('/indentlpc', methods=['GET','POST'])
def localpurchase():
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
		vendor_n=I['vendorname']
		print(vendor_n)

		cur.execute("INSERT INTO indentor(indent_date,handlename,Designation,indent_approving,Budget_type, estimated_cost,expected_delivery_period) VALUES ('"+indent_date+"','"+Name+"','"+Desgn+"','"+IAA+"','"+Radio+"','"+cost+"','"+expectdate+"');")
		connection.commit()
		cur.execute("SELECT max(indent_id) from indentor")
		indent_id=cur.fetchall()
		cur.execute("INSERT INTO main_cat(item_name,brand,quantity,warrenty_period) VALUES ('"+itemname+"','"+brand+"','"+qty+"','"+warrenty+"');")
		connection.commit()
		cur.execute("INSERT INTO sub_cat(item_specification) VALUES ('"+subcat+"');")
		connection.commit()
		cur.execute("INSERT INTO vendor(vendor_name, indent_id) VALUES ('"+vendor_n+"',"+str(indent_id[0][0])+");")
		connection.commit()
		cur.execute("INSERT INTO purchase_types(indent_id,local_purchase) VALUES("+str(indent_id[0][0])+",'localpurchase');")
		connection.commit()
		return redirect(url_for('message'))
	else:
		return render_template("indentlpc.html")

@app.route('/indentgem', methods=['GET','POST'])
def GEM():
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

		cur.execute("INSERT INTO indentor(indent_date,handlename,Designation,indent_approving,Budget_type, estimated_cost,expected_delivery_period) VALUES ('"+indent_date+"','"+Name+"','"+Desgn+"','"+IAA+"','"+Radio+"','"+cost+"','"+expectdate+"');")
		connection.commit()
		cur.execute("SELECT max(indent_id) from indentor")
		indent_id=cur.fetchall()
		cur.execute("INSERT INTO main_cat(item_name,brand,quantity,warrenty_period) VALUES ('"+itemname+"','"+brand+"','"+qty+"','"+warrenty+"');")
		connection.commit()
		cur.execute("INSERT INTO sub_cat(item_specification) VALUES ('"+subcat+"');")
		connection.commit()
		cur.execute("INSERT INTO purchase_types(indent_id,gem) VALUES("+str(indent_id[0][0])+",'gem');")
		connection.commit()
		return redirect(url_for('message'))

	else:
		return render_template("indentgem.html")
@app.route('/message')
def message():
	return render_template('message.html')

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
		return render_template("Admin.html")

@app.route('/admin_directpurchase', methods=['GET','POST'])
def admin_directpurchase():
	if request.method=='POST':
		f_id=request.form['place']
		print(f_id)
		return redirect(url_for('placeorder_directpurchase',f_id=f_id))
	else:
		cur.execute("SELECT indent_id from purchase_types where direct_purchase='directpurchase';")
		value=cur.fetchall()
		valuesize=len(value)
		print(type(value))
		print(value,"saloni")
		forms=[]
		for i in value:
			cur.execute("SELECT * from indentor where indent_id = "+str(i[0])+";")
			form=cur.fetchone()
			form=list(form)
			print(form,"QWERTYUIOP")
			print(type(form),"saloniibaba")
			forms.append(form)
			print(forms,"aniii")
		
		return render_template('admin_directpurchase.html',forms=forms)


@app.route('/admin_localpurchase', methods=['GET','POST'])
def admin_localpurchase() :
	if request.method=='POST':
		f_id=request.form['place']
		print(f_id)
		return redirect(url_for('placeorder_localpurchase',f_id=f_id))
	else:
		cur.execute("SELECT indent_id from purchase_types where local_purchase='localpurchase';")
		value=cur.fetchall()
		valuesize=len(value)
		print(type(value))
		print(value,"saloni")
		forms=[]
		for i in value:
			cur.execute("SELECT * from indentor where indent_id = "+str(i[0])+";")
			form=cur.fetchone()
			form=list(form)
			print(form,"QWERTYUIOP")
			forms.append(form)
		
		return render_template('admin_localpurchase.html',value=value, forms=forms)


@app.route('/admin_gem', methods=['GET','POST'])
def admin_gem() :
	if request.method=='POST':
		f_id=request.form['place']
		print(f_id)
		return redirect(url_for('placeorder_gem',f_id=f_id))


	else:
		cur.execute("SELECT indent_id from purchase_types where gem='gem';")
		value=cur.fetchall()
		valuesize=len(value)
		print(type(value))
		print(value,"saloni")
		forms=[]
		for i in value:
			cur.execute("SELECT * from indentor where indent_id = "+str(i[0])+";")
			form=cur.fetchone()
			form=list(form)
			print(form,"QWERTYUIOP")
			forms.append(form)
		
		return render_template('admin_gem.html',value=value, forms=forms)
@app.route('/placeorder_directpurchase', methods=['GET','POST'])
def placeorder_directpurchase():
	f_id=request.args.get('f_id')
	print(f_id,'qwertyui')
	cur.execute("SELECT handlename from indentor where indent_id = '"+f_id+"';")
	appr1 = cur.fetchall()
	print(appr1,'smit')
	connection.commit()
	cur.execute("SELECT expected_delivery_period from indentor where indent_id = '"+f_id+"';")
	appr2 = cur.fetchall()
	print(appr2,'saloni')
	connection.commit()
	cur.execute("SELECT vendor_name from vendor where indent_id = '"+f_id+"';")
	v_name=cur.fetchall()
	connection.commit()
	cur.execute("UPDATE indentor SET checkr = true where indent_id = '"+f_id+"';")
	connection.commit()
	if request.method=='POST':
		if 'approve' in request.form:
			return redirect(url_for('approval',f_id=f_id))
		elif 'bill' in request.form:
			cur.execute("SELECT handlename from indentor where indent_id = '"+f_id+"';")
			appr11 = cur.fetchall()
			cur.execute("SELECT expected_delivery_period from indentor where indent_id = '"+f_id+"';")
			appr22 = cur.fetchall()
			cur.execute("SELECT vendor_name from vendor where indent_id = '"+f_id+"';")
			v_name1=cur.fetchall()
			cur.execute("UPDATE indentor SET checkr = true where indent_id = '"+f_id+"';")
			connection.commit()
			cur.execute("UPDATE indentor SET order_date = CURDATE() where indent_id = '"+f_id+"';")
			connection.commit()
			cur.execute("UPDATE indentor SET order_status ='placed' where  indent_id = '"+f_id+"';")
			connection.commit();
			cur.execute("SELECT order_date from indentor where indent_id = '"+f_id+"';")
			bill=cur.fetchall()
			connection.commit()
			print("AAAAAAA")
			return redirect(url_for('bill',appr11=appr11, appr22=appr22,f_id=f_id,v_name1=v_name1,bill=bill))

	else:
		return render_template("placeorder_directpurchase.html",f_id=f_id)


@app.route('/placeorder_localpurchase', methods=['GET','POST'])
def placeorder_localpurchase():
	f_id=request.args.get('f_id')
	print("AAAAAAA")
	cur.execute("SELECT handlename from indentor where indent_id = '"+f_id+"';")
	appr1 = cur.fetchall()
	connection.commit()
	cur.execute("SELECT expected_delivery_period from indentor where indent_id = '"+f_id+"';")
	appr2 = cur.fetchall()
	connection.commit()
	print(appr1,"SDFGHJ")
	print(appr1,"SDFGHJ")
	cur.execute("SELECT vendor_name from vendor where indent_id = '"+f_id+"';")
	v_name=cur.fetchall()
	print(v_name[0][0])
	connection.commit()
	//print("AAAAAAA")
	cur.execute("UPDATE indentor SET checkr = true where indent_id = '"+f_id+"';")
	connection.commit()
	//print("AAAAAAA")
	if request.method=='POST':
		if 'approve' in request.form:
			return redirect(url_for('approval',appr1=appr1[0][0], appr2=appr2[0][0],f_id=f_id,v_name=v_name[0][0]))
		elif 'bill' in request.form:
			cur.execute("SELECT handlename from indentor where indent_id = '"+f_id+"';")
			appr11 = cur.fetchall()
			print(appr11,'salonisawarkar')
			cur.execute("SELECT expected_delivery_period from indentor where indent_id = '"+f_id+"';")
			appr22 = cur.fetchall()
			cur.execute("SELECT vendor_name from vendor where indent_id = '"+f_id+"';")
			v_name1=cur.fetchall()
			print(v_name[0])
			cur.execute("UPDATE indentor SET checkr = true where indent_id = '"+f_id+"';")
			connection.commit()
			cur.execute("UPDATE indentor SET order_date = CURDATE() where indent_id = '"+f_id+"';")
			connection.commit()
			cur.execute("UPDATE indentor SET order_status ='placed' where  indent_id = '"+f_id+"';")
			connection.commit();
			cur.execute("SELECT order_date from indentor where indent_id = '"+f_id+"';")
			bill=cur.fetchall()
			connection.commit()
			return redirect(url_for('bill',appr11=appr11[0][0], appr22=appr22[0][0],f_id=f_id,v_name1=v_name1[0][0],bill=bill))
	else:
		return render_template("placeorder_localpurchase.html",f_id=f_id)

@app.route('/placeorder_gem', methods=['GET','POST'])
def placeorder_gem():
	f_id=request.args.get('f_id')
	print("saloniiiiiii")
	cur.execute("SELECT handlename from indentor where indent_id = '"+f_id+"';")
	appr1 = cur.fetchall()
	connection.commit()
	cur.execute("SELECT expected_delivery_period from indentor where indent_id = '"+f_id+"';")
	appr2 = cur.fetchall()
	connection.commit()
	print(appr1,"SDFGHJ")
	print(appr1,"SDFGHJ")
	cur.execute("SELECT vendor_name from vendor where indent_id = '"+f_id+"';")
	v_name=cur.fetchall()
	connection.commit()
	cur.execute("UPDATE indentor SET checkr = true where indent_id = '"+f_id+"';")
	connection.commit()
	if request.method=='POST':
		if 'approve' in request.form:
			return redirect(url_for('approval',appr1=appr1[0][0], appr2=appr2[0][0],f_id=f_id))
		elif 'bill' in request.form:
			cur.execute("SELECT handlename,expected_delivery_period from indentor where indent_id = '"+f_id+"';")
			appr11= cur.fetchall()
			cur.execute("SELECT vendor_name from vendor where indent_id = '"+f_id+"';")
			v_name1=cur.fetchall()
			//print(v_name1[0])
			cur.execute("UPDATE indentor SET checkr = true where indent_id = '"+f_id+"';")
			connection.commit()
			cur.execute("UPDATE indentor SET order_date = CURDATE() where indent_id = '"+f_id+"';")
			connection.commit()
			cur.execute("UPDATE indentor SET order_status ='placed' where  indent_id = '"+f_id+"';")
			connection.commit();
			cur.execute("SELECT order_status,order_date from indentor where indent_id = '"+f_id+"';")
			bill=cur.fetchall()
			connection.commit()
			return redirect(url_for('bill',appr11=appr1[0][0],appr22=appr2[0][0],f_id=f_id,v_name1=v_name[0][0]))

	else:
		return render_template("placeorder_gem.html",f_id=f_id)

@app.route('/approval', methods=['GET','POST'])
def approval():
	f_id=request.args.get('f_id')
	if request.method == 'POST':
		return redirect(url_for('placeorder_directpurchase',f_id=f_id))

	else:
		return render_template('approve.html',f_id=f_id)

@app.route('/bills', methods=['GET','POST'])
def bill():
	appr11=request.args.get('appr11')
	appr22=request.args.get('appr22')
	f_id=request.args.get('f_id')
	v_name1=request.args.get('v_name1')
	print(appr11,"QWERTYUIOP")
	print(f_id)
	print("AAAAAAA")
	if 'OK1' in request.form:
			return redirect(url_for('Admin'))
	elif 'OK2' in request.form:
			return redirect(url_for('signin'))
	return render_template('bill.html',appr11=appr11, appr22=appr22,f_id=f_id,v_name1=v_name1)

if __name__ == '__main__':
	app.run(debug=True)
