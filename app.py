from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # यह templates फोल्डर के अंदर index.html को ढूंढेगा
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_password():
    password = request.form.get('password')
    # यहाँ आपका पासवर्ड चेक करने का लॉजिक आएगा
    length = len(password)
    
    if length < 6:
        result = "Weak"
    elif length < 10:
        result = "Medium"
    else:
        result = "Strong"
        
    return f"<h2>Password Strength: {result}</h2><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
