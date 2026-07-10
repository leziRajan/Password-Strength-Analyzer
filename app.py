# Password analyzer project - Submitted by Rajan
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_password():
    password = request.form.get('password')
    
    # basic variables for checking complexity
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    special_chars = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\"
    
    # looping through each character (human style coding)
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    # calculating score based on conditions
    score = 0
    if length >= 8: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    # final strength text and color logic
    if score <= 2:
        result = "Weak"
        color = "#ff4d4d"
    elif score <= 4:
        result = "Medium"
        color = "#ffa64d"
    else:
        result = "Strong"
        color = "#2db300"
        
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Result</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #f4f7f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 400px; width: 90%; text-align: center; }}
            h2 {{ color: #0c2340; }}
            .status {{ font-size: 24px; font-weight: bold; color: {color}; margin: 20px 0; }}
            a {{ display: inline-block; background: #1a66ff; color: white; text-decoration: none; padding: 10px 20px; border-radius: 5px; font-weight: bold; width: 80%; }}
            a:hover {{ background: #0052cc; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Analysis Result</h2>
            <div class="status">Strength: {result}</div>
            <p style="color: #666; font-size: 14px;">Total Length: {length}</p>
            <br>
            <a href="/">Go Back</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
