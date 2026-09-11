from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>DevTech Attendance Portal</title>
    </head>
    <body style="font-family:Arial;padding:30px">

        <h1>DevTech Attendance Portal</h1>
        <h3>Version 5.0</h3>

        <form>
            <label>Employee ID</label><br>
            <input type="text"><br><br>

            <label>Employee Name</label><br>
            <input type="text"><br><br>

            <label>Domain</label><br>
            <select>
                <option>Linux Admin</option>
                <option>Windows Admin</option>
                <option>Cloud Engineer</option>
                <option>DevOps Engineer</option>
            </select><br><br>

            <label>Date</label><br>
            <input type="date"><br><br>

            <label>Status</label><br>
            <input type="radio" name="status"> Present
            <input type="radio" name="status"> Absent
            <br><br>

            <button type="submit">Submit Attendance</button>
        </form>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
