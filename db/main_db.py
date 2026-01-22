from config import path_db
from db import queries
import sqlite3


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.tasks_table)

    conn.commit()
    conn.close()



def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_task, (task, ))
    conn.commit()
    task_id =cursor.lastrowid
    conn.close()
    return task_id


def update_task(task_id,new_task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.update_task, (new_task, task_id ))
    conn.commit()
    conn.close()
   

def dalete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.dalete_task, (task_id, ))
    conn.commit()
    conn.close()


def get_tasks(filter_type):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if filter_type =='all':
        cursor.execute(queries.select_task)
    elif filter_type == 'completed':
        cursor.execute(queries.select_task_completed)
    elif filter_type == 'uncompleted':
        cursor.exrcute(queries.select_task_uncompleted)
        
    task = cursor.fetchall()
    conn.close()
    return task
