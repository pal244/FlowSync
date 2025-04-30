from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend apps (like Kivy)

# Dummy in-memory user storage
users = {}  # Format: {username: password}

# Root route for testing
@app.route("/")
def home():
    return "FlowSync backend is running!"

# Signup route
@app.route("/api/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"success": False, "message": "Username and password are required."}), 400

    if username in users:
        return jsonify({"success": False, "message": "User already exists."}), 409

    users[username] = password
    return jsonify({"success": True, "message": "Signup successful!"}), 201

# Login route
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        return jsonify({"success": True, "message": "Login successful!"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid credentials."}), 401

# Optional: Save water intake
@app.route("/api/save_intake", methods=["POST"])
def save_intake():
    data = request.get_json()
    username = data.get("username")
    intake = data.get("intake")

    print(f"User {username} recorded {intake} ml of water.")  # Debug logging
    return jsonify({"success": True, "message": "Water intake saved."}), 200

if __name__ == "__main__":
    app.run(debug=True)
