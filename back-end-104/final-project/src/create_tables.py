# create_tables.py

from database import engine
from models import Base

# Создаём все таблицы, которые ещё не существуют
Base.metadata.create_all(bind=engine)

print("Таблицы успешно созданы!")
