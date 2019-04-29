from flask import Flask, request, render_template, redirect, url_for
from controller import add_student_to_db, show_student_details, delete_student_from_db, \
    edit_student, search_student_details

app = Flask(__name__)


@app.route('/')
def index(roll_number=None):
    if request.args:
        for i in request.args.items():
            roll_number = i[1]
    return render_template('index_2.html', student_data=show_student_details(),
                           search_student_data=search_student_details(roll_number=roll_number))


@app.route('/add', methods=['POST'])
def add():
    """
    this function takes the post request for addition of the student in database
    :return: redirect to the index
    """
    add_student_to_db(request.form)
    return redirect(url_for('index'))


@app.route('/delete/<int:roll_number>', methods=['POST'])
def delete(roll_number):
    """
    This function takes the roll number as the request parameter and delete the  student from the database
    :param roll_number:
    :return: redirect to index
    """
    if roll_number:
        delete_student_from_db(roll_number)
        return redirect(url_for('index'))


@app.route('/edit', methods=['POST'])
def edit():
    """
    this function takes the post request and edit the student
    :return: redirect to url
    """
    edit_student(request.form)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
