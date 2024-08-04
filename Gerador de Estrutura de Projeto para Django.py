import os
import subprocess

def create_django_project_structure(project_name):
    subprocess.run(['django-admin', 'startproject', project_name])
    os.chdir(project_name)
    subprocess.run(['python', 'manage.py', 'startapp', 'myapp'])
    print(f'Projeto Django "{project_name}" criado com sucesso!')

if __name__ == '__main__':
    project_name = input("Digite o nome do projeto Django: ")
    create_django_project_structure(project_name)
