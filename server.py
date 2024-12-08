"""
Servidor para levantamiento de instancia Flask de aplicación para Detector de emociones
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")

def render_index_page():
    """
    Pagina principal de Flask
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detector():
    """
    Endpoint para analizar emociones en un texto dado.

    Lee un parámetro 'textToAnalyze' desde la URL, lo procesa
    usando el detector de emociones y devuelve el resultado en formato JSON.

    Returns:
        Response: Un objeto JSON con las emociones analizadas o un mensaje de error.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    if response is None:
        response = "¡Texto inválido!, ¡Por favor, inténtalo de nuevo!"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
