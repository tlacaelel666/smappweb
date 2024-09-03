import os
from app import app  # Importa tu aplicación Flask

if __name__ == "__main__":
    app.run()
  PORT = int(os.environ.get('PORT'))
