from flask import Flask, request

app = Flask(__name__)

employees = {
    "sampath": {
        "id": "EMP001",
        "doj": "15-Feb-2022",
        "experience": "4 Years",
        "domain": "Linux / DevOps"
    },
    "ram": {
        "id": "EMP002",
        "doj": "10-Jun-2021",
        "experience": "5 Years",
        "domain": "Windows Admin"
    },
    "jay": {
        "id": "EMP003",
        "doj": "05-Jan-2023",
        "experience": "3 Years",
        "domain": "Cloud Engineer"
    },
    "ayyapa": {
        "id": "EMP004",
        "doj": "20-Mar-2022",
        "experience": "4 Years",
        "domain": "DevOps Engineer"
    },
    "siva": {
        "id": "EMP005",
        "doj": "11-Nov-2020",
        "experience": "6 Years",
        "domain": "Linux Administrator"
    }
}

@app.route("/")
def home():

    name = request.args.get("name", "").lower()

    result = ""

    if name in employees:
        emp = employees[name]

        result = f"""
        <div class="employee-card">
            <h2>Employee Details</h2>
            <p><b>Employee ID:</b> {emp['id']}</p>
            <p><b>Date Of Joining:</b> {emp['doj']}</p>
            <p><b>Experience:</b> {emp['experience']}</p>
            <p><b>Domain:</b> {emp['domain']}</p>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Employee Portal</title>

<style>

body {{
    margin:0;
    font-family:'Segoe UI',sans-serif;
    background:#eef3ff;
}}

.header {{
    background:linear-gradient(90deg,#005bea,#6f42ff);
    color:white;
    padding:20px;
    display:flex;
    justify-content:space-between;
}}

.sidebar {{
    position:fixed;
    top:78px;
    left:0;
    width:220px;
    height:100%;
    background:#081f5c;
    color:white;
}}

.sidebar ul {{
    list-style:none;
    padding:0;
}}

.sidebar li {{
    padding:18px;
    border-bottom:1px solid rgba(255,255,255,0.1);
}}

.main {{
    margin-left:240px;
    padding:30px;
}}

.cards {{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
}}

.card {{
    background:white;
    border-radius:15px;
    padding:20px;
    text-align:center;
    box-shadow:0 4px 10px rgba(0,0,0,.1);
}}

.card h2 {{
    margin:0;
    color:#005bea;
}}

.search {{
    margin-top:30px;
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0 4px 10px rgba(0,0,0,.1);
}}

input[type=text] {{
    width:70%;
    padding:12px;
    border:1px solid #ccc;
    border-radius:8px;
}}

button {{
    background:#005bea;
    color:white;
    border:none;
    padding:12px 25px;
    border-radius:8px;
    cursor:pointer;
}}

button:hover {{
    background:#0040b3;
}}

.employee-card {{
    margin-top:20px;
    background:#f7faff;
    border-left:5px solid #005bea;
    padding:20px;
    border-radius:10px;
}}

</style>
</head>

<body>

<div class="header">
    <h1>🚀 Coro infotech Employee Portal</h1>
    <h2>Version 7.0</h2>
</div>

<div class="sidebar">
<ul>
<li>🏠 Dashboard</li>
<li>👨 Employees</li>
<li>📅 Attendance</li>
<li>📊 Reports</li>
<li>⚙ Settings</li>
</ul>
</div>

<div class="main">

<div class="cards">

<div class="card">
<h2>5</h2>
<p>Total Employees</p>
</div>

<div class="card">
<h2>4</h2>
<p>Present</p>
</div>

<div class="card">
<h2>1</h2>
<p>Absent</p>
</div>

<div class="card">
<h2>80%</h2>
<p>Attendance Rate</p>
</div>

</div>

<div class="search">

<h2>Employee Search</h2>

<form method="get">

<input type="text"
name="name"
placeholder="Search Sampath, Ram, Jay, Ayyapa or Siva">

<button type="submit">
Search
</button>

</form>

{result}

</div>

</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
