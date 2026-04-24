# Запити до бази даних

from sqlite3 import Error

from connect import create_connection, database

import pandas as pd


def select_projects(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return: rows projects
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM projects;")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return: rows tasks
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_task_by_status(conn, status):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param status:
    :return: rows tasks
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks WHERE status=?", (status,))
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
        print("\\nQuery all tasks")
        tasks = select_all_tasks(conn)
        print(tasks)
        print("\\nQuery task by status:")
        task_by_priority = select_task_by_status(conn, True)
        print(task_by_priority)

'''Projects:
[(1, 'Cool App with SQLite & Python', '2022-01-01', '2022-01-30')]

Query all tasks
[(1, 'Analyze the requirements of the app', 1, 1, 1, '2022-01-01', '2022-01-02'), (2, 'Confirm with user about the top requirements', 1, 1, 0, '2022-01-03', '2022-01-05')]

Query task by status:
[(1, 'Analyze the requirements of the app', 1, 1, 1, '2022-01-01', '2022-01-02')]
'''



df = pd.DataFrame(projects, columns=[
    "id", "name", "start_date", "end_date"
])

print(df)
print(df.to_string(index=False))

df_tasks = pd.DataFrame(tasks, columns=[
    "id", "name", "priority", "project_id",
    "status", "begin_date", "end_date"
])

print(df_tasks)
