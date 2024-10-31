from sqlalchemy import create_engine, Connection
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool, NullPool
from contextlib import contextmanager


# Create a connection to the database
DATABASE_CONN ="mysql+mysqlconnector://root:1234@localhost:3306/blog_db"

# Engine 생성
engine = create_engine(DATABASE_CONN, 
                       poolclass=QueuePool,    # poolclass=NullPool,
                       pool_size=10, 
                       max_overflow=0,
                       pool_recycle=300) # 300초마다 재사용

def direct_get_conn():
    try: 
        conn = engine.connect()
        return conn
    except SQLAlchemyError as e:
        print(f'error: {e}')
        raise e   # 사용자가 일부러 에러를 발생시키는 경우


@contextmanager
def context_get_conn():
    try:
        conn = engine.connect()
        yield conn   # 제너에이터가  yield를 만나면 호출자에게 제어권을 넘겨줌
    except SQLAlchemyError as e:
        print(f'error: {e}')
        raise e
    finally:
        conn.close()
        print("connection is closed inside finally")

