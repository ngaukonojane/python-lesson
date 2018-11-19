from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    IntegerField,
                    OperationalError,
                    IntegrityError)
db = SqliteDatabase("students.db")
students = [
    {'id': 1, 'username': 'joycedev', 'name': 'Joyce', 'course': 'python', 'age': 18},
    {'id': 2, 'username': 'fatma15', 'name': 'Fatma', 'course': 'jave', 'age': 19}
]


class blog(Model):
    title = CharField(max_length=255, unique=True)
    body = CharField(max_length=1000)
    craeted_at = TextField(default="python")
    age = IntegerField(default=18)

    class Meta:
        database = db


def initialize():
    try:
        Student.create_table()
    except OperationalError:
        pass
    for student in students:
        try:
            Student.create(
                username=student.get('username'),
                name=student.get('name'),
                course=student.get('course'),
                age=student.get('age')
                )
        except IntegrityError:
            pass