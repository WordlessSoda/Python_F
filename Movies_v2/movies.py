from flask import Flask, render_template, request
from pymysql import connect
import requests, MySQLdb


app = Flask(__name__)


@app.route('/', methods=['GET'])
def entry() -> 'html':
    return render_template('entry.html')


@app.route('/result', methods=['POST'])
def result() -> 'html':
    title = '豆瓣电影Top250'
    top = request.form['id']
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='movies', charset='utf8')
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    try:
        if int(top)%1==0:  # 如果是排名，那么排名是int类型
            sql = "select * from movie where 排名='{}'".format(top)
    except:  # 如果是片名
        sql = "select * from movie where 片名 like '%{}%'".format(top)

    cursor.execute(sql)
    a = cursor.fetchall()
    cursor.close()
    conn.close()

    # for i in a:
    #     result = i
    #     print(result)

    return render_template('result.html',
                           the_result=a,
                           the_title=title,
                           the_top=top)


@app.route('/content')
def content() -> 'html':
    if request.method == "GET":
        title = '豆瓣电影Top250'
        req = request.args
        nam = req.get("nam")

        conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='movies', charset='utf8')
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        sql = "select * from movie where 片名='{}'".format(nam)
        print(sql)
        cursor.execute(sql)
        a = cursor.fetchall()
        cursor.close()
        conn.close()

        print(a)
        return render_template('content.html',
                               the_result=a,
                               the_title=title,
                               the_top=nam
                               )


if __name__ == '__main__':
    app.run(debug=True)
