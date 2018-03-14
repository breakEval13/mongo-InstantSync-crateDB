from crate import client

SERVER_IP="127.0.0.1:4200"
def conn(s):
    connection = client.connect(SERVER_IP)
    cursor = connection.cursor()
    print()
    if cursor.execute("show tables like '"+s+"'")=='None':
        print(s+"table is None")
    else:
      ret =  cursor.execute("""INSERT INTO doc.my_table (id, date, kind, position) VALUES (?, ?, ?, ?)""", ('123123123', '2007-03-11', 'Quasar', 7))
      print(ret)
conn('doc.my_table');