from flask import request, jsonify, redirect, url_for,render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity,get_jwt
from backend.models import *  # Ensure this import is correct
from flask import current_app as app  # Import 'app' from app.py

# Define role-based dashboard URLs
DASHBOARD_URLS = {
    "School": "/dashboard/school",
    "Parent": "/dashboard/parent",
    "Student": "/dashboard/student"
}

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")  # Plain text password
    role = data.get("role")

    if not email or not password or not role:
        return jsonify({"error": "Email, password, and role are required"}), 400

    user = User.query.filter_by(email=email, role=role, password=password).first()  # Direct match

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    # Get dashboard URL based on role
    dashboard_url = DASHBOARD_URLS.get(user.role, "/dashboard/default")

    return jsonify({
        "message": "Login successful",
        "token": access_token,
        "dashboard_url": dashboard_url  # Return dashboard route
    }), 200

@app.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    claims = get_jwt()  # Retrieve JWT claims
    user_id = get_jwt_identity()  # Get user ID
    role = claims.get("role")  # Get user role from JWT

    # Check if role exists in the claims
    if not role:
        return jsonify({"message": "Role not found in token"}), 401

    # Fetch user from DB
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    if role == "School":
        return render_template('school_dashboard.html', user=user)
    elif role == "Parent":
        return render_template('parent_dashboard.html', user=user)
    elif role == "Student":
        return render_template('student_dashboard.html', user=user)
    else:
        return jsonify({"message": "Role not recognized"}), 403

