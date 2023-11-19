import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    diff = {}

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        if key in data1 and key in data2:
            if data1[key] != data2[key]:
                diff['- ' + key] = data1[key]
                diff['+ ' + key] = data2[key]
        elif key in data1:
            diff['- ' + key] = data1[key]
        else:
            diff['+ ' + key] = data2[key]

    return json.dumps(diff, indent=2)


# Пример использования
file_path1 = 'file1.json'
file_path2 = 'file2.json'

diff = generate_diff(file_path1, file_path2)
print(diff)