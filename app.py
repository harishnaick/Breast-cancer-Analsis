import pickle
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Function to initialize database
def init_db():
    with sqlite3.connect('database.db') as conn:
        print("Opened database successfully")
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL);
        ''')
        print("Table created successfully")
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS contact_messages
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL);
        ''')
        print("Table created successfully")

# Initialize database
init_db()

# Load the trained model and scaler
def load_model_and_scaler():
    with open('logistic_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    return model, scaler

# Route to render signup form
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        email = request.form['email']

        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE email=?", (email,))
            existing_user = cur.fetchone()

            if existing_user:
                return "User with this email already exists. <a href='/signup'>Go back to Signup</a>"
            else:
                cur.execute("INSERT INTO users (name, password, email) VALUES (?, ?, ?)", (name, password, email))
                conn.commit()
                return redirect(url_for('login'))

    return render_template('signup.html')

# Route to render login form
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
            user = cur.fetchone()

            if user:
                session['user'] = user[0]
                return redirect(url_for('home'))
            else:
                return "Invalid email or password. <a href='{}'>Go back to Login</a>".format(url_for('login'))

    return render_template('login.html')

# Route to render home or index page
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/symptoms', methods=['POST', 'GET'])
def symptoms():
    if request.method == 'POST':
        symptom = request.form.get('symptom')
        
        if symptom == 'itching':
            return redirect(url_for('stage0'))
        elif symptom == 'lump':
            return redirect(url_for('stage1'))
        elif symptom == 'lump_breast_pain':
            return redirect(url_for('stage2'))
        elif symptom == 'blood_discharge':
            return redirect(url_for('stage3'))
        else:
            return "Invalid symptom selected"
    return render_template('symptoms.html')

@app.route('/stage0')
def stage0():
    return render_template('stage0.html')

@app.route('/stage1')
def stage1():
    return render_template('stage1.html')

@app.route('/stage2')
def stage2():
    return render_template('stage2.html')

@app.route('/stage3')
def stage3():
    return render_template('stage3.html')

# Route to render prediction form
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Load model and scaler
            model, scaler = load_model_and_scaler()

            # Extract data from form
            radius_mean = float(request.form['radius_mean'])
            texture_mean = float(request.form['texture_mean'])
            perimeter_mean = float(request.form['perimeter_mean'])
            area_mean = float(request.form['area_mean'])
            smoothness_mean = float(request.form['smoothness_mean'])
            compactness_mean = float(request.form['compactness_mean'])
            concavity_mean = float(request.form['concavity_mean'])
            concave_points_mean = float(request.form['concave_points_mean'])
            symmetry_mean = float(request.form['symmetry_mean'])
            fractal_dimension_mean = float(request.form['fractal_dimension_mean'])

            # Scale the input data
            user_input = np.array([
                [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
                 compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean]
            ])
            user_input_scaled = scaler.transform(user_input)

            # Make prediction
            prediction = model.predict(user_input_scaled)

            # Determine diagnosis result
            result = 'Malignant' if prediction[0] == 1 else 'Benign'

            # Store result in session for display in result.html
            session['result'] = result
            # Redirect to result page
            return redirect(url_for('show_result'))

        except KeyError as e:
            error_message = f"Missing form data key: {str(e)}"
            return f"Error: {error_message}. <a href='/predict'>Go back to Prediction Form</a>"

    return render_template('predict.html')
@app.route('/result')
def show_result():
    result = session.pop('result', None)  # Retrieve and clear result from session
    if result is None:
        return "No prediction result found. <a href='/predict'>Go back to Prediction Form</a>"
    return render_template('result.html', diagnosis=result)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Store the contact message into the database
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO contact_messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
            conn.commit()
        
        return redirect(url_for('home'))  # Redirect to a thank you page or another endpoint
    
    return render_template('contact.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
