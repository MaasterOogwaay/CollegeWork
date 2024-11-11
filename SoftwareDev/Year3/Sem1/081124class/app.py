"""
A sample Hello World server.
"""
import os

from flask import Flask, request, flash, url_for, redirect, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.secret_key = 'super secret key'
db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    age = db.Column(db.Integer)

    def __init__(self, name, city, addr, age):
        self.name = name
        self.city = city
        self.addr = addr
        self.age = age


db.create_all()

global_student=students('A','B','C',99) # Ensure Opening2, delete2 & update2 are referencing the same student

@app.route('/',methods=['GET', 'POST'])
def opening2():
    global global_student
    if request.method == 'POST':
        if 'Search_By_City' in request.form:
            if not request.form['city']:
                flash('Please enter all the city fields', 'error')
            else:
                searchCity= request.form['city']
                studentList = db.session.query(students).filter(students.city == searchCity).all()
                return render_template('show_all.html', message='Test', students=studentList)

        elif 'Search_By_Name' in request.form:
            if not request.form['name']:
                flash('Please enter all the name fields', 'error')
            else:
                searchName= request.form['name']
                student = db.session.query(students).filter(students.name == searchName).first()
                return render_template('search.html', message='Test', student=student)

        elif 'Delete_Student' in request.form:
            if not request.form['name']:
                flash('Please enter all the name fields', 'error')
            else:
                searchName= request.form['name']
                student = db.session.query(students).filter(students.name == searchName).first()
                global_student = student
                return redirect(url_for('delete2', student=student))

        elif 'Update_Student' in request.form:
            if not request.form['name']:
                flash('Please enter all the name fields', 'error')
            else:
                searchName= request.form['name']
                student = db.session.query(students).filter(students.name == searchName).first()
                global_student = student
                return redirect(url_for('update2', student=student))

        elif 'Increment_Student_Age' in request.form:
            if not request.form['name']:
                flash('Please enter all the name fields', 'error')
            else:
                searchName= request.form['name']
                student = db.session.query(students).filter(students.name == searchName).first()
                global_student = student
                return redirect(url_for('increment_age2', student=student))

    all_data3 = db.session.query(students).all()
    return render_template('opening2.html', message='test' ,students=all_data3)

@app.route('/search', methods=['GET', 'POST'])
def search():

    return render_template('search.html')

@app.route('/delete2', methods=[ 'GET','POST'])
def delete2():
    searchName = 'abc'
    if request.method == 'POST':
        if not request.form['name']:
            flash('Please enter all the fields', 'error')
        else:
            searchName = request.form['name']
            student = db.session.query(students).filter(students.name == searchName).first()
            db.session.delete(student)
            db.session.commit()
            return redirect(url_for('show_all'))

    searchStudent = global_student
    return render_template('delete2.html', student=searchStudent)



@app.route('/update2', methods=[ 'GET','POST'])
def update2():
    searchName = 'abc'
    if request.method == 'POST':
        if not request.form['name']:
            flash('Please enter all the fields', 'error')
        else:
            updateName = request.form['name']
            student = db.session.query(students).filter(students.name == updateName).first()
            student.city = request.form['city']
            student.addr =  request.form['addr']
            student.age  = request.form['age']
            db.session.commit()

            print('Record was successfully updated')
            return redirect(url_for('show_all'))
    searchStudent = global_student

    return render_template('update2.html', student=searchStudent)


@app.route('/increment_age2', methods=[ 'GET','POST'])
def increment_age2():
    searchName = 'abc'
    if request.method == 'POST':
        if not request.form['name']:
            flash('Please enter all the fields', 'error')
        else:
            updateName = request.form['name']
            student = db.session.query(students).filter(students.name == updateName).first()
            age  = int(request.form['age'])
            student.age = age+1
            db.session.commit()
            return redirect(url_for('show_all'))

    searchStudent = global_student
    return render_template('increment_age2.html', student=searchStudent)




@app.route('/show_all', methods=['GET', 'POST'])
def show_all():
    all_data3 = db.session.query(students).all()
    return render_template('show_all.html', message='test' ,students=all_data3)


@app.route('/initial_table_data', methods=['GET', 'POST'])
def initial_table_data():
    if request.method == 'POST' :
        print('here')
        db.session.add(students('J.Smith', 'Dublin', 'Tallagh', 22))
        db.session.add(students('W.Shine', 'Athlone', 'Monksland', 27))
        db.session.add(students('T.Jones', 'Athlone', 'Dublin Road', 35))
        db.session.add(students('P.Dodds', 'Galway', 'Cliften', 21))
        db.session.add(students('Tony Potts', 'Galway', 'Salthill Rd', 48))
        db.session.commit()
        flash('Initial Table Data Added')

    return render_template('initial_table_data.html')



@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'], request.form['city'],
                               request.form['addr'], request.form['age'])

            db.session.add(student)
            db.session.commit()
            return redirect(url_for('show_all'))
    return render_template('new.html')




if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')



