# Доступ до бази даних з Python

'''методи підключення до бази даних:
close() — закриття з'єднання;
commit() — зафіксувати будь-яку відкладену транзакцію в базу даних;
rollback() — викликає відкочування бази даних до початку будь-якої очікуваної транзакції. 
Закриття з'єднання без попередньої фіксації змін спричинить неявне відкочування;
cursor() — повернути новий об'єкт курсора за допомогою поточного з'єднання.
'''

'''Курсор — це об’єкт, через який Python “спілкується” з базою даних.
курсор = “інструмент”, який виконує SQL-запити і отримує результат

cursor.execute(sql) 👉 виконати один SQL-запит

cursor.executemany(sql, data) 👉 виконати багато запитів одразу (швидше)

cursor.close() 👉 закрити курсор (звільнити ресурси)

Отримання даних:

cursor.fetchone() 👉 отримати 1 рядок

cursor.fetchmany(5) 👉 отримати кілька рядків

cursor.fetchmany(5) 👉 отримати кілька рядків

'''

from sqlite3 import Error

from connect import create_connection, database

def select_projects(conn):
    """
    Query all rows in the projects table with its tasks
    :param conn: the Connection object
    :return: rows projects or None
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM projects JOIN tasks ON tasks.project_id = projects.id;")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows

if __name__ == '__main__':
    with create_connection(database) as conn:
        print("Projects:")
        projects = select_projects(conn)
        print(projects)

'''Projects:
[(1, 'Cool App with SQLite & Python', '2022-01-01', '2022-01-30', 2, 'Confirm with user about the top requirements', 1, 1, 1, '2022-01-03', '2022-01-05')]
'''