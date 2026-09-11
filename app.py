return f"""
<!DOCTYPE html>
<html>
<head>
<title>DevTech Attendance Portal</title>

<style>

body {{
    margin:0;
    font-family:Segoe UI, sans-serif;
    background:#eef4ff;
}}

.header {{
    background:linear-gradient(90deg,#005bea,#6f42ff);
    color:white;
    padding:20px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}}

.header h1 {{
    margin:0;
}}

.sidebar {{
    position:fixed;
    top:80px;
    left:0;
    width:240px;
    height:100%;
    background:#0b1f59;
    color:white;
    padding-top:20px;
}}

.sidebar a {{
    display:block;
    color:white;
    padding:15px 25px;
    text-decoration:none;
}}

.sidebar a:hover {{
    background:#3f51ff;
}}

.main {{
    margin-left:260px;
    padding:30px;
}}

.card {{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0 4px 12px rgba(0,0,0,0.1);
    margin-bottom:20px;
}}

.grid {{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px;
}}

input, select {{
    width:100%;
    padding:12px;
    border:1px solid #ccc;
    border-radius:10px;
}}

button {{
    background:linear-gradient(90deg,#0099ff,#7a3cff);
    color:white;
    border:none;
    padding:15px;
    width:100%;
    border-radius:12px;
    font-size:18px;
    cursor:pointer;
}}

.stats {{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:15px;
}}

.stat-box {{
    background:white;
    text-align:center;
    padding:20px;
    border-radius:15px;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
}}

.present {{
    border-left:5px solid green;
}}

.absent {{
    border-left:5px solid red;
}}

.total {{
    border-left:5px solid blue;
}}

.rate {{
    border-left:5px solid purple;
}}

.search-box {{
    display:flex;
    gap:10px;
}}

.search-box input {{
    flex:1;
}}

</style>
</head>

<body>

<div class="header">
    <h1>🚀 DevTech Attendance Portal</h1>
    <h2>Version 6.0</h2>
</div>

<div class="sidebar">
    #🏠 Dashboard</a>
    #📅 Attendance</a>
    #👨‍💼 Employees</a>
    #📊 Reports</a>
    #⚙ Settings</a>
    #🚪 Logout</a>
</div>

<div class="main">

<div class="stats">

<div class="stat-box present">
<h2>24</h2>
<p>Present</p>
</div>

<div class="stat-box absent">
<h2>6</h2>
<p>Absent</p>
</div>

<div class="stat-box total">
<h2>30</h2>
<p>Total Employees</p>
</div>

<div class="stat-box rate">
<h2>80%</h2>
<p>Attendance Rate</p>
</div>

</div>

<br>

<div class="card">

<h2>🔍 Employee Search</h2>

<form method="get">

<div class="search-box">

<input
type="text"
name="name"
placeholder="Enter Sampath, Ram, Jay, Ayyapa or Siva">

<button type="submit">
Search
</button>

</div>

</form>

<br>

{result}

</div>

<div class="card">

<h2>📝 Mark Attendance</h2>

<div class="grid">

<div>
<label>Employee ID</label>
<input type="text" placeholder="EMP001">
</div>

<div>
<label>Employee Name</label>
<input type="text" placeholder="Sampath">
</div>

<div>
<label>Domain</label>
<select>
<option>Linux Admin</option>
<option>Windows Admin</option>
<option>Cloud Engineer</option>
<option>DevOps Engineer</option>
</select>
</div>

<div>
<label>Date</label>
<input type="date">
</div>

</div>

<br>

<label>Status</label><br><br>

<input type="radio" name="status"> Present
&nbsp;&nbsp;&nbsp;
<input type="radio" name="status"> Absent

<br><br>

<button>
Submit Attendance
</button>

</div>

</div>

</body>
</html>
"""
