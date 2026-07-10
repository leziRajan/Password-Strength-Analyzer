from flask import Flask, request, render_template_string
import re
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "index.html file not found in repository!", 404

@app.route('/check', methods=['POST'])
def check_password():
    password = request.form.get('password') or ""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase (A-Z) and lowercase (a-z) letters.")

    if re.search(r"[ !@#$%^&*(),.?\":{}|<>_+-]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., @, #, $, %).")

    if score == 4:
        result = "Strong 🔥"
        color = "green"
    elif score >= 2:
        result = "Medium ⚠️"
        color = "orange"
    else:
        result = "Weak ❌"
        color = "red"

    suggestions = "".join([f"<li>{f}</li>" for f in feedback]) if feedback else "<li>Your password is perfect and secure!</li>"

    response_html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Result</title>
    </head>
    <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background: #f4f7f6;">
        <div style="background: white; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 400px; width: 90%;">
            <h2 style="color: #0c2340;">Password Strength Result</h2>
            <h1 style="color: {color}; margin: 20px 0;">{result}</h1>
            
            <h3 style="text-align: left; color: #333;">Suggestions:</h3>
            <ul style="text-align: left; padding-left: 20px; color: #555; line-height: 1.6;">
                {suggestions}
            </ul>
            <br>
            <a href="/" style="display: inline-block; text-decoration: none; background: #1a66ff; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">Go Back</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(response_html)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
