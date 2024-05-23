from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hearing_test') #url
def hearing_test():
    return render_template('hearing_test.html') #source

@app.route('/bpm_test')  #url
def bpm_test():
    return render_template('bpm_test.html')  #source

if __name__ == '__main__':
    app.run(debug=True)