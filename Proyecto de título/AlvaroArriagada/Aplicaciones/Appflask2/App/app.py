from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def actor() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'sakila'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM actor')
    results = [{actor_id: first_name} for (actor_id, first_name, last_name, last_update) in cursor]
    cursor.execute("USE sakila")
    cursor.close()
    connection.close()
    return results


@app.route('/', methods=['GET'])
def home():
    return '''<h1>API Sakila</h1>
<p>Un prototipo de API para la base de datos Sakila.</p>'''

@app.route('/actor')
def index() -> str:
    return json.dumps({'actor': actor()})

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
