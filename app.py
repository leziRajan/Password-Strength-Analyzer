from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_password():
    password = request.form.get('password')
    score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    # 2. Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    # 3. Uppercase & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase (A-Z) and lowercase (a-z) letters.")

    # 4. Special Character Check
    if re.search(r"[ !@#$%^&*(),.?\":{}|<>_+-]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., @, #, $, %).")

    # Result Determining
    if score == 4:
        result = "Strong 🔥"
        color = "green"
    elif score >= 2:
        result = "Medium ⚠️"
        color = "orange"
    else:
        result = "Weak ❌"
        color = "red"

    # Response HTML page (Fixed Go Back Link)
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
                {"".join([f"<li>{f}</li>" for f in feedback]) if feedback else "<li>Your password is perfect and secure!</li>"}
            </ul>
            <br>
            <a href="index.html" style="display: inline-block; text-decoration: none; background: #1a66ff; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">Go Back</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(response_html)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


