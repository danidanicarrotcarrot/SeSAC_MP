from flask import Flask, render_template, request

app = Flask(__name__)

# 첫 페이지 (과제 1, 과제 2 링크)
@app.route('/')
def index():
    return render_template('index.html')

# 과제 1: username 입력받고 변환
@app.route('/task1', methods=['GET', 'POST'])
def task1():
    result = None
    if request.method == 'POST':
        username = request.form['username']
        if len(username) % 2 == 0:
            result = username.upper()
        else:
            result = username.lower()
    return render_template('task1.html', result=result)

# 과제 2: 구구단 출력
@app.route('/task2', methods=['GET', 'POST'])
def task2():
    result = None
    if request.method == 'POST':
        try:
            num = int(request.form['number'])
            result = [f"{num} × {i} = {num * i}" for i in range(1, 10)]
        except ValueError:
            result = ["숫자를 입력하세요."]
    return render_template('task2.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)