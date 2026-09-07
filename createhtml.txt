import pandas as pd
import sqlite3

# 1. Connect to SQLite database
conn = sqlite3.connect("todo.db")

# 2. Read query into a DataFrame
df = pd.read_sql_query("SELECT * FROM tasks", conn)

# 3. Convert to HTML with basic Bootstrap table classes
# Note: DataTables will automatically add specific styling, but we give it a clean base
bootstrap_table = df.to_html(index=False, classes="table table-striped table-hover table-bordered table-responsive" )

# 4. Wrap it in a Bootstrap 5.3 + DataTables template
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To do</title>
    
    <!-- Bootstrap 5.3 CSS CDN -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    
    
    
</head>
<body>
    <div class="container mt-5">
        <h2 class="mb-4 text-center">Tasks</h2>
        
        <!-- Table container for mobile responsiveness -->
        <div class="table-responsive p-2 shadow-sm rounded border bg-white text-center">
            {bootstrap_table}
        </div>
    </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>

  
</body>
</html>"""

# 5. Save the template
with open("table_functional.html", "w", encoding="utf-8") as f:
    f.write(full_html)

conn.close()
print("Bootstrap table created in 'table_functional.html'!")
