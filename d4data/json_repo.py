from .data_access.json_access import load_json_data

def LocalJSONRepo(path):
    data = load_json_data(path)
    if isinstance(data, dict):
        pass
    elif isinstance(data, list):
        pass


