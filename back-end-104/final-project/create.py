from src.database import SessionLocal
from src.models import User, UserProfile, UserAchievement, Quest, QuestProgress, Achievement

db = SessionLocal()

new_user = User(
  id=1,
  name='adilkhan',
  email='abibos@gmail.com',
  password_hash='b10jsdfasdfasodf'
)

db.add(new_user)
db.commit()
db.refresh(new_user)