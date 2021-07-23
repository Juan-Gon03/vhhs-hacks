from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/info/')
def info():
    return render_template('info.html')

@app.route('/moreInfo/')
def moreInfo():
    return render_template('moreInfo.html')
    
if __name__ == "__main__":
    app.run(debug=True)