from flask import Flask, render_template, request, jsonify
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static',
            static_url_path='')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        # Log contact form submission
        print(f"Contact form submission: {name}, {email}")
        
        return jsonify({'status': 'success', 'message': 'Thank you for your message!'})
    
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/logo-preview')
def logo_preview():
    return render_template('logo_preview.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500
