from app import db

class Student(db.Model):
    __tablename__='student'
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(100),nullable = False)
    last_name = db.Column(db.String(100),nullable = False)
    gender_id = db.Column(db.Integer,db.ForeignKey('gender.id'),nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    age = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    user = db.relationship('User', back_populates='student')
    student_card = db.relationship('StudentCard', back_populates='student', uselist=False)
    gender = db.relationship('Gender', back_populates='students')
    
    def __repr__(self):
        return f'Student ({self.id},{self.first_name},{self.last_name},{self.email},{self.age})'

class Gender(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_latin = db.Column(db.String(10),nullable = False)
    acronym = db.Column(db.String(4),nullable = False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    students = db.relationship('Student', back_populates='gender')
    
    def __repr__(self):
        return f'Gender ({self.id},{self.name_latin},{self.acronym})'

class StudentCard(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    card_number = db.Column(db.String(20),unique = True,nullable=False)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'),unique = True,nullable=False)
    issued_date = db.Column(db.Date,nullable = False)
    expired_date = db.Column(db.Date,nullable = False)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    
    student = db.relationship('Student', back_populates='student_card', uselist=False)
    
    def __repr__(self):
        return f'StudentCard ({self.id},{self.card_number},{self.issued_date},{self.expired_date})'