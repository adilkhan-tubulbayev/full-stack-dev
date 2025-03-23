import enum
from datetime import datetime
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import Enum
from sqlalchemy import DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
class UserRole(enum.Enum):
  STUDENT = "student"
  TEACHER = "teacher"
  ADMIN = "admin"

class UserStatus(enum.Enum):
  ACTIVE = "active"
  INACTIVE = "inactive"

class LevelDifficulty(enum.Enum):
  EASY = "easy"
  MEDIUM = "medium"
  HARD = "hard"

class QuestStatus(enum.Enum):
  NOT_STARTED = "not_started"
  IN_PROGRESS = "in_progress"
  COMPLETED = "completed"
  FAILED = "failed"

class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key = True, index = True)
  name: Mapped[str] = mapped_column(String(100), unique = True, nullable = False)
  email: Mapped[str] = mapped_column(String(100), unique = True, nullable = False)
  password_hash: Mapped[str] = mapped_column(String(255), nullable = False)
  role: Mapped[UserRole] = mapped_column(Enum(UserRole), server_default = UserRole.STUDENT.value)
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now(), onupdate = func.now())

  profile: Mapped["UserProfile"] = relationship(
    back_populates = "user",
    uselist = False,
    cascade = "all, delete-orphan"
  )

  quests: Mapped[List["QuestProgress"]] = relationship(
    back_populates = "user",
    cascade = "all, delete-orphan"
  )

  achievements: Mapped[List["UserAchievement"]] = relationship(
    back_populates = "user",
    cascade = "all, delete-orphan"
  )
class UserProfile(Base):
  __tablename__ = "user_profiles"

  id: Mapped[int] = mapped_column(primary_key = True, index = True)
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
  display_name: Mapped[str] = mapped_column(String(50))
  avatar_url: Mapped[str] = mapped_column(String(255))
  coins: Mapped[int] = mapped_column(Integer, server_default = 0)
  level: Mapped[int] = mapped_column(Integer, server_default = 1)
  experience: Mapped[int] = mapped_column(Integer, server_default = 0)

  user: Mapped["User"] = relationship(
    back_populates = "profile"
  )

class Quests(Base):
  __tablename__ = "quests"

  id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
  title: Mapped[str] = mapped_column(String(255), nullable = False)
  description: Mapped[str] = mapped_column(Text)
  reward_coins: Mapped[int] = mapped_column(Integer, server_default = 0)
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now(), onupdate = func.now())

  progresses: Mapped[List["QuestProgress"]] = relationship(
    back_populates = "quest",
    cascade = "all, delete-orphan"
  )

class QuestProgress(Base):
  __tablename__ = "quest_progress"
  __table_args__ = (UniqueConstraint("user_id", "quest_id", name = "uq_user_quest"))

  id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
  quest_id: Mapped[int] = mapped_column(Integer, ForeignKey("quests.id"))
  status: Mapped[QuestStatus] = mapped_column(Enum(QuestStatus), server_default = QuestStatus.NOT_STARTED.value)
  started_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now())
  completed_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now(), onupdate = func.now())
  score: Mapped[int] = mapped_column(Integer, server_default = 0)

  quest: Mapped["Quests"] = relationship(
    back_populates = "progresses"
  )

  user: Mapped["User"] = relationship(
    back_populates = "quests"
  )

class Achievement(Base):
  __tablename__ = "achievements"

  id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
  name: Mapped[str] = mapped_column(String(100), nullable = False)
  description: Mapped[str] = mapped_column(Text)
  reward_coins: Mapped[int] = mapped_column(Integer, server_default = 0)
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now(), onupdate = func.now())

  user_achievements: Mapped[List["UserAchievement"]] = relationship(
    back_populates = "achievement",
    cascade = "all, delete-orphan"
  )
class UserAchievement(Base):
  __tablename__ = "user_achievements"
  __table_args__ = (UniqueConstraint("user_id", "achievement_id", name = "uq_user_achievement"))

  id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
  achievement_id: Mapped[int] = mapped_column(Integer, ForeignKey("achievements.id"))
  achieved_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now(), onupdate = func.now())

  user: Mapped["User"] = relationship(
    back_populates = "achievements"
  )

  achievement: Mapped["Achievement"] = relationship(
    back_populates = "user_achievements"
  )