from flask import render_template, Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html', title='главная', template_folder='../templates', static_folder='../static')
if __name__ == '__main__':
    app.run(debug=True)