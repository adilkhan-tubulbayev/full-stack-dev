from database import SessionLocal
from models import User

db = SessionLocal()

all_users = db.query(User).all()

for user in all_users:
  print(user)