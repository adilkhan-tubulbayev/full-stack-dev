from database import SessionLocal
from models import User

db = SessionLocal()

db.query(User).delete()
db.commit()