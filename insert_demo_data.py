import readFile
import load_to_sqlite

if __name__ == '__main__':
    demofile=r'C:\Users\vuth1\OneDrive\Desktop\demo.xlsx'
    conn = load_to_sqlite.open_connection()
    readFile.readfile(demofile,conn,tag_name='demo')
    conn.commit()
    conn.close()
