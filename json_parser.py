import json

def parse_to_var(file, var):
    f = open(file)
    data = json.load(f)
    f.close()

    return data[var]