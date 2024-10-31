from sqlalchemy import text, Connection
from sqlalchemy.exc import SQLAlchemyError
from database import direct_get_conn
from datetime import datetime

try:
    # Connection 얻기
    conn = direct_get_conn()

    # SQL 선언 및 text로 감싸기
    # 1, 2, 3, 4 | '둘리', '길동'
    query = "select id, title, author from blog where id = :user or \
        author = :author and modified_dt < :date"    
    stmt = text(query)
    bind_stmt = stmt.bindparams(user=1, author="길동", date=datetime.now())
    print(bind_stmt)
    
    # SQL 호출하여 CursorResult 반환. 
    result = conn.execute(bind_stmt)
    rows = result.fetchall() # row Set을 개별 원소로 가지는 List로 반환. 
    print(rows)
    result.close()
except SQLAlchemyError as e:
    print("############# ", e)
    #raise e
finally:
    # close() 메소드 호출하여 connection 반환.
    conn.close()