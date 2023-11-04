from flask import Flask, render_template
import util

app = Flask(__name__)

username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/')

def index():
    log = '''Hello! Welcome to our HW3 submission. 
        Please navigate to /api/update_basket_a to insert a row into basket_a, 
        or /api/unique to view a table of all unique entries in basket_a and basket_b.'''
    return render_template('index.html', log_html = log)

@app.route('/api/update_basket_a')

def update_basket_a():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor, "SELECT * from basket_a WHERE a = 5;")
    if record == -1:
        log = "Something is wrong with the SQL command"
    else:
        record = util.run_and_fetch_sql(cursor, "INSERT INTO basket_a VALUES (5, 'Cherry');")
        log = "Row (5, 'Cherry') inserted into basket_a."

    return render_template('/api/update_basket_a/update_basket_a.html', log_html = log)

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)