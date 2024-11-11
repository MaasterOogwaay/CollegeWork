"""
A sample Hello World server.
"""
import os

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    pin = db.Column(db.Integer)

    def __init__(self, name, city, addr, pin, age):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin
        self.age = age


db.create_all()
# Inserts records into a mapping table
db.session.add(students('J.Smith', 'Dublin', 'Tallagh', 111, 25))
db.session.add(students('W.Shine', 'Athlone', 'Monksland', 111, 78))
db.session.add(students('T.Jones', 'Athlone', 'Dublin Rd', 111, 28))
db.session.add(students('P.Dodds','Galway',     'Cliften', 111, 11))


query_objects= db.session.query(students)
myObject= query_objects.filter(students.city=='Athlone').first()
print()
print('First Student from Athlone is ' ,myObject.name)

print()
print('All Student    ')
print('-------------------------')
for el in query_objects.all():
    print (el.name, '\t',el.city, '\t', el.addr, '\t', el.age)
print('\n')

print()
print('Athlone Students    ')
print('-------------------------')
for el in query_objects.all():
    if el.city == "Athlone":
        print(el.name, '\t', el.city, '\t', el.addr)
print('\n')

print('Young Students    ')
print('-------------------------')
for el in query_objects.all():
    if el.age < 30:
        print(el.name, '\t', el.city, '\t', el.addr, '\t', el.age)
print('\n')

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "It's running Paul!"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
