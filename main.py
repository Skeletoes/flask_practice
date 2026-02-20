from flask import Flask, g, render_template
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def home():
    sql = "SELECT ModelName, Description, Year, EngineType, Displacement, Horsepower, BasePrice, ImageURL FROM Motorbikes;"
    results = query_db(sql)
    return render_template('home.html', results=results)

@app.route('/bike/<id>')
def bike(id):
    sql = "SELECT ModelName, Description, Year, EngineType, Displacement, Horsepower, BasePrice, ImageURL FROM Motorbikes WHERE ModelName = ?;"
    result = query_db(sql, (id,), True)
    return render_template('bike.html', bike=result)

if __name__ == '__main__':
    app.run(debug=True)
