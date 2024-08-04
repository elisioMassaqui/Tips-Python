import shutil
import os
from datetime import datetime

def backup_files(source_dir, backup_dir):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'backup_{timestamp}')
    shutil.copytree(source_dir, backup_path)
    print(f'Backup realizado com sucesso em {backup_path}')

if __name__ == '__main__':
    source_dir = input("Digite o diretório de origem: ")
    backup_dir = input("Digite o diretório de backup: ")
    backup_files(source_dir, backup_dir)
