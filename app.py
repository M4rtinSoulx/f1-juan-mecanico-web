import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'python_packages'))

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
      <head>
        <title>F1 Juan Mecánico</title>
        <style>
          body { font-family: Arial, sans-serif; background: #050505; color: #f2f2f2; margin: 0; padding: 0; }
          .page { max-width: 900px; margin: 0 auto; padding: 40px; text-align: center; }
          h1 { color: #ffcc00; margin-bottom: 0.5rem; }
          p { font-size: 1.1rem; line-height: 1.6; }
        </style>
      </head>
      <body>
        <div class="page">
          <h1>F1 Juan Mecánico</h1>
          <p>Bienvenido al pit stop digital donde preparamos el monoplaza para la próxima carrera.</p>
          <p>El backend Flask está listo para recibir peticiones y mostrar el estado del equipo.</p>
        </div>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)