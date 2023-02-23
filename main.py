from airtable import Airtable

from flask import Flask, render_template
import pandas as pd

# Configurar la conexión a la base de datos de Airtable
base_key = 'appTsErgl1kPnkWgl'
table_name = 'Contacts'
api_key = 'keykY5YjFxN23izT6'

airtable = Airtable(base_key, table_name, api_key)

# Obtener todos los registros de la tabla
records = airtable.get_all()
df = pd.DataFrame.from_records([record['fields'] for record in records])


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=df.to_html(classes = 'my_class" id = "my_id'))

if __name__ == '__main__':
    app.run(debug=True)