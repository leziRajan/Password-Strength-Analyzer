from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_password():
    password = request.form.get('password')
    length = len(password)
    
    # स्ट्रेंथ चेक करने का लॉजिक और उसका कलर
    if length < 6:
        result = "Weak"
        color = "#ff4d4d" # लाल रंग
    elif length < 10:
        result = "Medium"
        color = "#ffa64d" # ऑरेंज रंग
    else:
        result = "Strong"
        color = "#2db300" # हरा रंग
        
    # रिजल्ट पेज को भी सुंदर CSS कार्ड में रेंडर करना
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
            <br>
            <a href="/">Go Back</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
