
import sqlite3

tango = input('insert word: ')
print(tango)

# データベースに接続
conn = sqlite3.connect('dictionary.db')

# カーソルを作成
cursor = conn.cursor()

# テーブルの一覧を取得するSQLクエリ
table_list_query = "SELECT word, wordtype, definition FROM entries WHERE word LIKE ?"

# SQLクエリを実行
rows = cursor.execute(table_list_query, (tango,))
result = ""
for n in rows:
    result += f"【{n[0]}】{n[1]} {n[2]}\n"
    print(result)

# 接続を閉じる
conn.close()