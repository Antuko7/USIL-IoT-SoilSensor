from flask import Flask, render_template, jsonify
import random  # Para simular datos aleatorios de sensor y GPS

app = Flask(__name__)

# Ruta para servir la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener los datos del sensor y GPS
@app.route('/data')
def get_data():
    # Simular datos aleatorios de GPS y sensor de humedad
    data = {
        'lat': random.uniform(-12.080, -12.070),
        'lng': random.uniform(-76.960, -76.940),
        'speed': random.randint(0, 120),
        'humidity': random.randint(0, 100)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
