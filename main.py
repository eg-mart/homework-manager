from flask import Flask, render_template
from database import db_session
from database.users import User

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    port = 5000
    session = db_session.create_session()
    with session.begin():
        user = User(name="Даня", grade="11-1", priorities="физика", schedule="{}")
        user.set_password("12345678")
        session.add(user)

    app.run(host='0.0.0.0', port=port)

