from flask import Flask, render_template, request





app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')




@app.route("/clases", methods=['GET'])
def clases():
    return render_template('clases.html')









if __name__=='__main__':
    app.run(debug=True)