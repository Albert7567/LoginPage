from flask import Flask, request, jsonify, render_template, redirect, session
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)
app.secret_key = 'some_very_secret_key'

cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/verify', methods=['POST'])
def verify():
    try:
        id_token = request.json['idToken']
        decoded_token = auth.verify_id_token(id_token)
        session['user'] = decoded_token['uid']
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    return redirect('/')
