from model import Session, Student

session = Session()


def add_student_to_db(student_details):
    if student_details:
        row = Student(name=student_details['name'],
                      age=student_details['age'],
                      gender=student_details['gender'])
        session.add(row)
        session.commit()
        return 'Data added succcessfully'


def search_student_details(roll_number=None):
    if roll_number:
        all_students = session.query(Student).filter_by(roll_number=roll_number).all()
        data = {}
        for i in all_students:
            student_data = {}
            student_data['roll_number'] = i.roll_number
            student_data['name'] = i.name
            student_data['age'] = i.age
            student_data['gender'] = i.gender
            data[i.roll_number] = student_data
        return data
    else:
        return {}


def show_student_details(roll_number=None):
    data = {}
    if roll_number:
        all_students = session.query(Student).filter_by(roll_number=roll_number).all()
    else:
        all_students = session.query(Student).all()
        if not all_students:
            data = None

    for i in all_students:
        student_data = {}
        student_data['roll_number'] = i.roll_number
        student_data['name'] = i.name
        student_data['age'] = i.age
        student_data['gender'] = i.gender
        data[i.roll_number] = student_data

    return data


def delete_student_from_db(roll_number):
    student_detail = session.query(Student).filter_by(roll_number=roll_number).first()
    session.delete(student_detail)
    session.commit()


def edit_student(student_edit_details=None):
    student_detail = session.query(Student).filter_by(roll_number=student_edit_details['roll_number']).first()
    if student_detail:
        if student_edit_details.__getitem__('name'):
            student_detail.name = student_edit_details['name']
        if student_edit_details.__getitem__('age'):
            student_detail.age = student_edit_details['age']
        if student_edit_details.__getitem__('gender'):
            student_detail.gender = student_edit_details['gender']
        session.commit()
        return True
    else:
        return False
