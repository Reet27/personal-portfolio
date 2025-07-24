from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Email configuration (optional - for contact form)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-app-password'     # Replace with your app password

mail = Mail(app)

@app.route('/')
def home():
    """Home page with personal information"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page with detailed information"""
    return render_template('about.html')

@app.route('/projects')
def projects():
    """Projects showcase page"""
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact form page"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if name and email and message:
            # Here you can add email sending logic
            flash('Thank you for your message! I\'ll get back to you soon.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'error')
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)