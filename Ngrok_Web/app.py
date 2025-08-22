from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)
PUBLIC_DIR = os.path.expanduser("~/Public")

# Template HTML stylisé
TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>📂 Partage Public</title>
  <style>
    body { font-family: Arial, sans-serif; background: #1e1e2e; color: #fff; text-align: center; padding: 20px; }
    h1 { color: #4cafef; }
    .files-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 25px;
      margin-top: 20px;
    }
    .file-card {
      background: #2a2a3c;
      width: 160px;
      height: 160px;
      border-radius: 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      text-align: center;
      padding: 10px;
      transition: transform 0.2s, background 0.2s;
      cursor: pointer;
    }
    .file-card:hover {
      transform: scale(1.1);
      background: #3c3c52;
    }
    .file-name {
      font-weight: bold;
      word-break: break-word;
      color: #ffcc00;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-grow: 1;
    }
    .download-btn {
      background-color: #4cafef;
      border: none;
      color: black;
      padding: 5px 10px;
      font-size: 12px;
      border-radius: 5px;
      cursor: pointer;
      transition: background 0.2s;
      text-decoration: none;
    }
    .download-btn:hover {
      background-color: #2196f3;
    }
    .icon {
      font-size: 40px;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <h1>📂 Bienvenue dans mon dossier Public</h1>
  <p>Cliquez sur le carré pour afficher le fichier dans le navigateur ou utilisez le bouton pour télécharger :</p>
  <div class="files-container">
    {% for file, size, is_dir in files %}
      <div class="file-card" onclick="window.location='/public/{{ file }}'">
        {% if is_dir %}
          <div class="icon">📁</div>
        {% else %}
          <div class="icon">📄</div>
        {% endif %}
        <div class="file-name">{{ file }}</div>
        {% if not is_dir %}
          <a href="/public/{{ file }}" download class="download-btn">Télécharger</a>
        {% endif %}
      </div>
    {% endfor %}
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    files = []
    for f in os.listdir(PUBLIC_DIR):
        path = os.path.join(PUBLIC_DIR, f)
        is_dir = os.path.isdir(path)
        files.append((f, os.path.getsize(path) if not is_dir else 0, is_dir))
    return render_template_string(TEMPLATE, files=files)

@app.route("/public/<path:filename>")
def serve_file(filename):
    return send_from_directory(PUBLIC_DIR, filename, as_attachment=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8765)
