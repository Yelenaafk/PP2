from connect import get_connection, create_table

def call_search(pattern):
    conn = get_connection()
    if conn is None:
        print("Connection failed.")
        return
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def call_upsert(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

create_table()
if __name__ == "__main__":
    call_search("a")
    call_upsert("Alice", "123456")
    call_upsert("Satoru", "52522525")