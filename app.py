from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>DevTech Attendance Portal</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 80px;">
        <h1>DevTech Attendance Portal</h1>
        <hr>
        <h2>Welcome to DevTech.com</h2>
        <p>Employee Attendance Management System</p>
        <p>Status: Application Running Successfully ✅</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
