import os
import subprocess

def create_simple_flask_project_structure(project_name):
    base_dir = project_name

    # Diretórios principais
    directories = [
        base_dir,
        os.path.join(base_dir, 'templates')
    ]

    # Criação dos diretórios
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f'Diretório criado: {directory}')

    # Arquivos principais
    files = {
        os.path.join(base_dir, 'app.py'): """from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
""",
        os.path.join(base_dir, 'templates', 'index.html'): """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Flask App</title>
</head>
<body>
    <h1>Welcome to Flask!</h1>
</body>
</html>
"""
    }

    # Criação dos arquivos
    for file_path, content in files.items():
        with open(file_path, 'w') as file:
            file.write(content)
            print(f'Arquivo criado: {file_path}')

    # Abrir o diretório no VS Code em uma nova janela
    # Abrir o Visual Studio Code em uma nova janela
    subprocess.run(['code.cmd', '--new-window'])

if __name__ == '__main__':
    project_name = input("Digite o nome do projeto Flask: ")
    create_simple_flask_project_structure(project_name)
    print(f'Estrutura do projeto Flask \"{project_name}\" criada com sucesso!')
