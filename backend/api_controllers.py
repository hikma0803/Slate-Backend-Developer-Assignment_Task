from flask_restful import Resource,Api
from flask import request, jsonify
from .models import *
from datetime import datetime
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

api=Api()

# API Endpoint to Fetch Student Achievements
class StudentAchievements(Resource):
    @jwt_required()
    def get(self, student_id):
        user_email = get_jwt_identity()
        user = User.query.filter_by(email=user_email).first()

        if not user:
            return {"message": "User not found"}, 404

        # Check access permission
        if user.role == "School" or (user.role in ["Parent", "Student"] and user.linked_student_id == student_id):
            achievements = StudentAchievement.query.filter_by(student_id=student_id).all()
            return jsonify([{"id": ach.id, "achievement": ach.achievement} for ach in achievements])

        return {"message": "Unauthorized access"}, 403

# Add Resource to API
api.add_resource(StudentAchievements, "/student/achievements/<int:student_id>")
