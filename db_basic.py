from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError

# Create a connection to the database
DATABASE_CONN ="mysql+mysqlconnector://root:1234@localhost:3306/blog_db"

# Engine 생성
engine = create_engine(DATABASE_CONN, 
                       poolclass=QueuePool, 
                       pool_size=10, 
                       max_overflow=0)

try:
    # Connection 생성
    conn = engine.connect()
    # SQL 선언 및 text로 변환
    sql = "SELECT id, title FROM blog"
    stmt = text(sql)

    # Query 실행 : SQL 호출 => CursorResult 반환
    result = conn.execute(stmt)
    print(f'type result: {result}')

    # CursorResult에서 데이터 추출
    rows = result.fetchall()
    print(f'type rows: {rows}')

    # print(type(rows))
    print("======================")
    print(rows[0])
    print(rows[0][0]," / ", rows[0][1])
    print(rows[0].id," / ", rows[0].title)
    print(rows[0]._key_to_index)

    result.close()

except SQLAlchemyError as e:
    print(f'error: {e}')

finally:
    # Connection 반환 => Pool에 반환
    conn.close()



