from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    file = instance.dequeue()
    lines = txt_importer(file)
    list_file = list()
    result = list()

    for index, line in enumerate(lines):
        if (word in line):
            list_file.append({"linha": index + 1})
        if (len(list_file) > 0):
            result.append({
                "palavra": word,
                "arquivo": file,
                "ocorrencias": list_file
            })
        return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
