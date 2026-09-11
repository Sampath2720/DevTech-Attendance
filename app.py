from flask import Flask, request

app = Flask(__name__)

employees = {
    "sampath": {"id":"EMP001","doj":"15-Feb-2022","experience":"4 Years","domain":"Linux / DevOps"},
    "ram": {"id":"EMP002","doj":"10-Jun-2021","experience":"5 Years","domain":"Windows Admin"},
    "jay": {"id":"EMP003","doj":"05-Jan-2023","experience":"3 Years","domain":"Cloud Engineer"},
    "ayyapa": {"id":"EMP004","doj":"20-Mar-2022","experience":"4 Years","domain":"DevOps Engineer"},
    "siva": {"id":"EMP005","doj":"11-Nov-2020","experience":"6 Years","domain":"Linux Admin"}
}

@app.route("/")
def home():
    name = request.args.get("name", "").lower()

    result = ""

    if name in employees:
        emp = employees[name]
        result = f"""
        <h2>Employee Details</h2>
        <p><b>Employee ID:</b> {emp['id']}</p>
        <p><b>Date of Joining:</b> {emp['doj']}</p>
        <p><b>Experience:</b> {emp['experience']}</p>
        <p><b>Domain:</b> {emp['domain']}</p>
        """

    return f"""
    <html>
    <body style="font-family:Arial;text-align:center">
        <h1>DevTech Employee Portal</h1>
        <h3>Version 6.0</h3>

        <form method="get">
            <input type="text" name="name" placeholder="Enter Employee Name">
            <button type="submit">Search</button>
        </form>

        {result}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
