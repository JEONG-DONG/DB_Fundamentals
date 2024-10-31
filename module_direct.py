from sqlalchemy import text, Connection
from sqlalchemy.exc import SQLAlchemyError
from database import direct_get_conn

def execute_query(conn: Connection):
    query = "select * from blog"
    stmt = text(query)
    # SQL 호출하여 CursorResult 반환. 
    result = conn.execute(stmt)

    rows = result.fetchall()
    result.close()
    return rows

def execute_sleep(conn: Connection):
    query = "select sleep(5)"
    result = conn.execute(text(query))
    result.close()

for ind in range(20):
    try: 
        # database.py의 direct_get_conn() 호출 => Connection 생성 함수
        conn = direct_get_conn()
        execute_sleep(conn)  
        print("loop index:", ind)
    except SQLAlchemyError as e:
        print(e)
    finally: 
        conn.close()
        print("connection is closed inside finally")

print("end of loop")


# conn = direct_get_conn()
# rows = execute_query(conn)
# print(f"rows: {rows}")
# conn.close()



