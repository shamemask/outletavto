import os

with open('files_list.txt', 'w') as output_file:
    for root, dirs, files in os.walk('.'):
        if '\\venv' not in root and '\\node_modules' not in root and '\\build' not in root and '\\.git' not in root \
                and '\\.idea' not in root and '__pycache__' not in root:
            print(root)
            for file in files:
                if file.endswith(( '.py', '.html')) and file != 'get_all_codes.py' and file != 'Dockerfile':
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path)
                    output_file.write("file " + rel_path + '\n' + "'''" + '\n')
                    print(file_path)
                    with open(file_path, 'r',encoding='utf8') as input_file:
                        file_contents = input_file.read()
                        output_file.write(file_contents + "\n'''\n\n")