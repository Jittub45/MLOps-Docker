from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Form</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .form-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        input[type="text"] {
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .submit-btn {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .submit-btn:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <form action="/greet" method="POST">
            <label for="username">Enter your name:</label>
            <input type="text" name="username" id="username" required>
            <br>
            <input type="submit" value="Submit" class="submit-btn">
        </form>
    </div>
</body>
</html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form['username']
    return f"<h2 style='text-align:center; font-family:Arial;'>Hello {user_input}, Welcome to this app for Docker demonstration. Nice to meet You!!.</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
