import logging
import uuid
from flask import Flask, render_template, request
from flask_sessionstore import Session
from flask_session_captcha import FlaskSessionCaptcha

app = Flask(__name__)

# Nome do arquivo de banco de dados sqlite
data_base = 'myapp.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + data_base

# Captcha Configuration
app.config["SECRET_KEY"] = uuid.uuid4()
app.config['CAPTCHA_ENABLE'] = True
# Set 5 as character length in captcha
app.config['CAPTCHA_LENGTH'] = 5
# Set the captcha height and width
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60
app.config['CAPTCHA_SESSION_KEY'] = 'captcha_image'
app.config['SESSION_TYPE'] = 'sqlalchemy'

# Enables server session
Session(app)

# Initialize FlaskSessionCaptcha
captcha = FlaskSessionCaptcha(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if captcha.validate():
            return "success"
        else:
            return "fail"
    return render_template('form.html')

if __name__ == "__main__":
    app.debug = True
    logging.getLogger().setLevel("DEBUG")
    app.run()