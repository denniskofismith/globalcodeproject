from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# def get_class_data():
#     conn = sqlite3.connect('final.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM motion_log ORDER BY timestamp DESC')
#     rows = cursor.fetchall()
#     conn.close()
#     return rows

def get_latest_status():
    conn = sqlite3.connect('final.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM motion_log ORDER BY timestamp DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    return row




@app.route('/')
def index():
    data = get_latest_status()
    
    # Default status
    class_status = 'Class Available'
    timestamp = 'No data available'
    
    if data:
        timestamp, status = data[1], data[2]
        if status == 'Motion Detected':
            class_status = 'Class Unavailable'
        
        # timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    return render_template('text.html', class_status=class_status, timestamp=timestamp)


# @app.route('/')
# def index():
#     data = get_class_data()
#     available_classes = []
#     unavailable_classes = []

#     for row in data:
#         timestamp, status = row[1], row[2]
#         if status == 'Motion Detected':
#             unavailable_classes.append((timestamp, status))
#         else:
#             available_classes.append((timestamp, status))
    
#     return render_template('final.html', available_classes=available_classes, unavailable_classes=unavailable_classes)

if __name__ == "__main__":
    app.run(debug=True)



































































# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# app = Flask(__name__)

# # Database connection function
# def get_db_connection():
#     conn = sqlite3.connect('motion_sensor.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.route('/')
# def index():
#     conn = get_db_connection()
#     logs = conn.execute('SELECT * FROM motion_log ORDER BY timestamp DESC').fetchall()
#     conn.close()
#     return render_template('final.html', logs=logs)

# @app.route('/add_log', methods=['POST'])
# def add_log():
#     status = request.form['status']
#     conn = get_db_connection()
#     conn.execute('INSERT INTO motion_log (status) VALUES (?)', (status,))
#     conn.commit()
#     conn.close()
#     return redirect(url_for('index'))

# if __name__ == "__main__":
#     app.run(debug=True)
