from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app

db = SQLAlchemy()

# Users Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'School', 'Parent', 'Student'
    linked_student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=True)

# Students Table 
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    school_name = db.Column(db.String(100), nullable=False)
    achievements = db.relationship('StudentAchievement', backref='student', lazy=True)

# Student Achievements Table
class StudentAchievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    achievement = db.Column(db.String(255), nullable=False)

