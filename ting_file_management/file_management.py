import sys


# https://www.delftstack.com/pt/howto/python/python-print-to-stderr/
def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, mode="r") as file:
            return file.read().split('\n')
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
