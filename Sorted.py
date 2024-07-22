def combine_files(file_names, output_file):
    files_data = []
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            files_data.append((file_name, len(lines), lines))
    files_data.sort(key=lambda x: x[1])
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_name, line_count, lines in files_data:
            out_file.write(f"{file_name}\n{line_count}\n")
            out_file.writelines(lines)
            out_file.write("\n")

file_names = ['1.txt', '2.txt', '3.txt']
output_file = 'result.txt'
combine_files(file_names, output_file)

with open(output_file, 'r', encoding='utf-8') as file:
    print(file.read())
