import sqlite3


def find_syns(word):
    conn = sqlite3.connect('synsets_ua.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id_set FROM wlist WHERE word = ?", (word,))
    result = cursor.fetchone()

    if result:
        id_set = result[0]
        cursor.execute("SELECT word FROM wlist WHERE id_set = ?", (id_set,))
        synonyms = cursor.fetchall()
        conn.close()
        return synonyms
    else:
        conn.close()
        return []



words= ["білий", "червоний", "зелений"]

for word in words:
    syns = find_syns(word)
    print(f"Синоніми для слова '{word}':")
    if syns:
        for synonym in syns:
            print(synonym[0])
    else:
        print("Синоніми не знайдено.")
