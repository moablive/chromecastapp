import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for
from flask_basicauth import BasicAuth

app = Flask(__name__)

# --- Configuração da Senha ---
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('PASSWORD', 'admin') # Pega do Docker
app.config['BASIC_AUTH_FORCE'] = True # Obriga login

basic_auth = BasicAuth(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action', methods=['POST'])
def action():
    cmd = request.form.get('command')
    url = request.form.get('url')
    
    # Monta o comando base
    catt_cmd = ["catt"]
    
    try:
        if cmd == "cast" and url:
            print(f"📺 Casting: {url}")
            subprocess.Popen(["catt", "cast", url]) # Popen para não travar a página
        
        elif cmd == "stop":
            subprocess.run(["catt", "stop"])
            
        elif cmd == "pause":
            subprocess.run(["catt", "play_toggle"]) # Alterna entre play/pause
            
        elif cmd == "vol_up":
            subprocess.run(["catt", "volumeup"])
            
        elif cmd == "vol_down":
            subprocess.run(["catt", "volumedown"])

    except Exception as e:
        print(f"Erro: {e}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    # Roda na porta 5000
    app.run(host='0.0.0.0', port=5000)
