import json

def _get_path(file_name):
    return f"data/{file_name}.json"

def create(file_name):
    data = []  # estrutura inicial
    with open(_get_path(file_name),"w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    return data

def open_create(file_name):
    try:
        with open(_get_path(file_name), "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return create(file_name)
    except json.JSONDecodeError:
        # Arquivo existe mas está vazio ou corrompido
        return create(file_name)

def save(file_name,data):
    with open(_get_path(file_name), "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    
def remove(file_name, index):
    data = open_create(file_name)

    try:
        removed = data.pop(index)
        save(file_name, data)
        print(f"Removido: {removed}")
    except IndexError:
        print("Índice inválido")