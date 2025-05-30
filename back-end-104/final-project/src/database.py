from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)  

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
