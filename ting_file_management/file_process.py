import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)
    accomplished = False

    # https://www.w3schools.com/python/ref_func_range.asp
    for index in range(len(instance)):
        if instance.search(index) == path_file:
            accomplished = True

    if not accomplished:
        instance.enqueue(path_file)
    sys.stdout.write(str({
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content
    }))


def remove(instance):
    if not len(instance):
        sys.stdout.write("Não há elementos\n")
    else:
        sys.stdout.write(
            f"Arquivo {instance.dequeue()} removido com sucesso\n"
        )


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        file_content = txt_importer(path_file)

        sys.stdout.write(str({
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_content),
            "linhas_do_arquivo": file_content
        }))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
