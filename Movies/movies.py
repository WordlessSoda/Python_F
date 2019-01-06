from flask import Flask,render_template,request
from pymysql import connect
import requests,MySQLdb

app = Flask(__name__)


@app.route('/',methods=['GET'])
def entry()-> 'html':
    return render_template('entry.html')
	

 
 
@app.route('/result',methods=['POST'])	
def result()-> 'html':
	title = '豆瓣电影Top250'
	top = str(request.form['id'])
	conn = MySQLdb.connect(host = '127.0.0.1',port = 3306 ,user = 'root',passwd = '', db = 'movies',charset = 'utf8')
	cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
	sql = "select * from movie where 排名='{}'".format(top)
	cursor.execute(sql)
	a = cursor.fetchall()
	cursor.close()
	conn.close()
	for i in a:
		result = i		
	return render_template('result.html',
							the_result=result,
							the_title=title,
							the_top=top)
	

	
if __name__ == '__main__':
	app.run(debug=True) 