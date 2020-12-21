file_en = './file_en.txt'
file_ja = './file_ja.txt'

# ファイルをリストで読み込み
with open(file_en, 'r', encoding="utf-8") as f:
    data_en = f.readlines()

with open(file_ja, 'r', encoding="utf-8") as f:
    data_jp = f.readlines()
    
insert_count = 1
for index, line in enumerate(data_jp):
    insert_index = index + insert_count
    if (line != "\n" and line != " \n"):
        line = '<br/>' + line
        data_en.insert(insert_index, line)
        insert_count += 1

with open(file_en, mode="w") as f:
    f.writelines(data_en)