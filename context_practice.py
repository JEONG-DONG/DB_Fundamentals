from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool, NullPool

# database connection URL
DATABASE_CONN ="mysql+mysqlconnector://root:1234@localhost:3306/blog_db"

# Engine 생성
engine = create_engine(DATABASE_CONN, 
                       poolclass=QueuePool, 
                       pool_size=10, 
                       max_overflow=0)

print("##### eninge created #####")

def context_execute_sleep():
    with engine.connect() as conn:
        query = "select sleep(5)" # mysql에게 5초간 sleep
        result = conn.execute(text(query))
        result.close()
        # conn.close()

for ind in range(20):
    print("loop index:", ind)
    context_execute_sleep()


print("end of loop")