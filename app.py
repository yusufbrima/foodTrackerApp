from flask import Flask, request, url_for, redirect,render_template,session,escape,g
from datetime import datetime 
from database import connect_db,get_db
app =  Flask(__name__)

app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "iuhto743yto34iuho287gh78"

@app.teardown_appcontext
def close_db(error):
	if(hasattr(g,'sqlite_db')):
		g.sqlite_db.close()

@app.route("/",methods=['POST','GET'])
@app.route("/index",methods=['GET'])
@app.route("/home",methods=['GET'])
def index():
	db =  connect_db()
	if(request.method=='POST'):
		date =  request.form['date']
		db_date =  datetime.strptime(date,"%Y-%m-%d") #yyyy-mm-dd
		final_date =  datetime.strftime(db_date,"%Y%m%d") ## yyyymmdd
		#pretty_date = datetime.strftime(db_date,"%B %d, %Y")#January 12, 1990
		db.execute("INSERT INTO log_date(entry_date) VALUES(?)",(final_date,))
		db.commit()
	cur =  db.execute("SELECT log_date.entry_date, SUM(food.protein) AS total_protein,SUM(food.carbohydrates) \
		AS total_carbohydrates,SUM(food.fat) AS total_fat,SUM(food.calories) AS \
		total_calories FROM log_date LEFT JOIN food_date ON food_date.log_date_id =  log_date.id \
		LEFT JOIN food on food.id =  food_date.food_id \
		GROUP BY log_date.id ORDER BY log_date.entry_date DESC")
	results =  cur.fetchall()
	data_result =  [] 
	for i in results:
		single_date =  {}
		single_date['date'] =  i['entry_date']
		single_date['protein'] =  i['total_protein']
		single_date['fat'] =  i['total_fat']
		single_date['carbohydrates'] =  i['total_carbohydrates']
		single_date['calories'] =  i['total_calories']
		d =  datetime.strptime(str(i['entry_date']),'%Y%m%d')
		single_date['entry_date'] =  datetime.strftime(d,"%B %d, %Y")
		data_result.append(single_date)


	return render_template("home.html",results=data_result)
	
@app.route("/view/<date>",methods=['GET','POST'])
def view(date):
	db =  connect_db()
	cur =  db.execute("SELECT id,entry_date FROM log_date WHERE entry_date=?",[date])
	date_result =  cur.fetchone()  
	if request.method =='POST':
		print(date_result['id'])
		db.execute("INSERT INTO food_date(food_id,log_date_id) VALUES(?,?)",(request.form['food'],date_result['id']))
		db.commit()

	d =  datetime.strptime(str(date_result['entry_date']),'%Y%m%d')
	pretty_date =  datetime.strftime(d,"%B %d, %Y")

	cur =  db.execute("SELECT id, name FROM food ORDER BY name")
	result =  cur.fetchall()

	log_cur =  db.execute("SELECT food.name, food.protein, food.carbohydrates,food.fat,food.calories \
		FROM log_date JOIN food_date ON food_date.log_date_id =  log_date.id \
		JOIN food on food.id =  food_date.food_id WHERE log_date.entry_date=?",[date])

	log_result =  log_cur.fetchall()

	totals = {} 
	totals['protein'] = 0 
	totals['carbohydrates'] = 0
	totals['fat'] =  0
	totals['calories'] =  0 
	for food in log_result:
		totals['protein'] +=  food['protein']
		totals['carbohydrates'] += food['carbohydrates']
		totals['fat'] += food['fat']
		totals['calories'] += food['calories']

	return render_template("day.html",result =  result,entry_date=date_result['entry_date'], pretty_date=  pretty_date, \
		log_result=log_result,totals =  totals)

@app.route("/food",methods=['POST','GET'])
def food():
	db = get_db()
	if(request.method=='POST'):
		foodName =  request.form['foodName']
		protein =  int(request.form['protein'])
		carbohydrates =  int(request.form['carbohydrates'])
		fat =  int(request.form['fat'])
		calories =  protein *4 + carbohydrates * 4 + fat * 9
		db.execute("INSERT INTO food (name,protein,carbohydrates,fat,calories) VALUES(?,?,?,?,?)",(\
			foodName,protein,carbohydrates,fat,calories))
		db.commit()
	cur =  db.execute("SELECT name,protein,carbohydrates,fat,calories FROM food")
	results =  cur.fetchall()
	return render_template("add_food.html",results = results)
if __name__ == '__main__':
	app.run("localhost",80,debug=True)