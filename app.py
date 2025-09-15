from flask import Flask, request, jsonify
import joblib
import numpy as np

# Cargar el modelo y el escalador
modelo = joblib.load('modelo_logistic_regression.pkl')
escalador = joblib.load('escalador.pkl')

# Crear la app Flask
app = Flask(__name__)

# Ruta para verificar el estado del servicio
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "API Breast Cancer Logistic Regression activa"}), 200

# Ruta para hacer predicciones
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Validar que el JSON tenga el campo 'features'
        if not data or 'features' not in data:
            return jsonify({"error": "Falta el campo 'features'"}), 400

        features = data['features']

        # Validar que sea una lista con la cantidad correcta de elementos
        if not isinstance(features, list) or len(features) != 30:
            return jsonify({"error": "El campo 'features' debe ser una lista de 30 valores"}), 400

        # Validar que todos los elementos sean numéricos
        if not all(isinstance(x, (int, float)) for x in features):
            return jsonify({"error": "Todos los valores en 'features' deben ser numéricos"}), 400

        # Escalar los datos
        features_scaled = escalador.transform([features])

        # Realizar la predicción
        prediction = modelo.predict(features_scaled)

        return jsonify({"prediction": int(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


