from flask import Flask, render_template
from database import db_session
from database.users import *
from sqlalchemy.orm import with_polymorphic


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port)

