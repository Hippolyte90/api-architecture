""" Database configuration"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db" # The database from our directory

## Create a database engine which establishes the connection with our SQLite database (movies.db)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Define SessionLocal, which allow to create the sessions for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define Base class for SQLAlchemy modles to inherit from
Base = declarative_base()

# if __name__ == "__main__":
#     try:
#         with engine.connect() as conn:
#             print("Database connection successful.")
#     except Exception as e:
#         print(f"Database connection failed: {e}")

