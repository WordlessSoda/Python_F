from flask import Flask, render_template, request
import requests
import jsonpath 

app = Flask(__name__)

def district(keywords,subdistrict=None)->str:
    parameters = {'keywords': keywords,'subdistrict':subdistrict,'key': '953be07c0895088279ef0c9d7a3532b6'}
    base = 'https://restapi.amap.com/v3/config/district?parameters'
    response = requests.get(base, parameters)
    answer = response.json()
    return str(jsonpath.jsonpath(answer,'$..name')) # 提取多层嵌套json中所需的值，返回列表

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = '这是查询结果:'
    results = district(phrase, letters)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='欢迎使用高德地图行政区域查询网站')


if __name__ == '__main__':
    app.run(debug=True)
