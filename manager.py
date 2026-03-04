import json

def create():
    data = []  # estrutura inicial
    with open("time_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    return data

def open_create():
    try:
        with open("time_data.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return create()
    except json.JSONDecodeError:
        # Arquivo existe mas está vazio ou corrompido
        return create()

def save(data):
    with open("time_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    
