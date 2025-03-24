from database import engine
from models import Base

# creating tables based on models.py objects
Base.metadata.create_all(bind=engine)

print("Tables added/updated successfully!")
