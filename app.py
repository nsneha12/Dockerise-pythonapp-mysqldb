from flask import Flask

import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/styles.css">
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    '''

@app.route('/countries')
def countries():
    cnx = mysql.connector.connect(
        host='db',
        user='root',
        password='secret',
        database='country_capital'
    )

    cursor = cnx.cursor()
    query = "SELECT country, capital FROM countries"
    cursor.execute(query)
    result = cursor.fetchall()

    countries_table = '<table>'
    countries_table += '<tr><th>Country</th><th>Capital</th></tr>'
    for row in result:
        country = row[0]
        capital = row[1]
        countries_table += f'<tr><td>{country}</td><td>{capital}</td></tr>'
    countries_table += '</table>'

    cursor.close()
    cnx.close()

    return f'<h1>Countries and Capitals</h1>{countries_table}'

