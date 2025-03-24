import enum
from datetime import datetime
from typing import List, Optional
from sqlalchemy import ForeignKey, String, Integer, Text, Enum, DateTime, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func

class UserRole(enum.Enum):
  STUDENT = "STUDENT"
  TEACHER = "TEACHER"
  ADMIN = "ADMIN"

class UserStatus(enum.Enum):
  ACTIVE = "ACTIVE"
  INACTIVE = "INACTIVE"

class LevelDifficulty(enum.Enum):
  EASY = "EASY"
  MEDIUM = "MEDIUM"
  HARD = "HARD"

class QuestStatus(enum.Enum):
  NOT_STARTED = "NOT_STARTED"
  IN_PROGRESS = "IN_PROGRESS"
  COMPLETED = "COMPLETED"
  FAILED = "FAILED"

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

  def __repr__(self):
    return f"<User id={self.id!r} name={self.name!r} email={self.email!r}>"

class UserProfile(Base):
  __tablename__ = "user_profiles"
  __table_args__ = (UniqueConstraint("user_id", name = "uq_user_profile"),)

  id: Mapped[int] = mapped_column(primary_key = True, index = True)
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", name="fk_user_profiles_user_id"))
  display_name: Mapped[str] = mapped_column(String(50))
  avatar_url: Mapped[str] = mapped_column(String(255))
  coins: Mapped[int] = mapped_column(Integer, CheckConstraint("coins >= 0"), server_default = "0")
  level: Mapped[int] = mapped_column(Integer, CheckConstraint("level >= 1"), server_default = "1")
  experience: Mapped[int] = mapped_column(Integer, CheckConstraint("experience >= 1"), server_default = "1")

  user: Mapped["User"] = relationship(
    back_populates = "profile"
  )

class Quests(Base):
  __tablename__ = "quests"

  id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
  title: Mapped[str] = mapped_column(String(255), nullable = False)
  description: Mapped[str] = mapped_column(Text)
  difficulty: Mapped[LevelDifficulty] = mapped_column(Enum(LevelDifficulty), server_default = LevelDifficulty.EASY.value)
  reward_coins: Mapped[int] = mapped_column(Integer, CheckConstraint("coins >= 0"), server_default = "0")
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now(), onupdate = func.now())

  progresses: Mapped[List["QuestProgress"]] = relationship(
    back_populates = "quest",
    cascade = "all, delete-orphan"
  )

class QuestProgress(Base):
  __tablename__ = "quest_progress"
  __table_args__ = (UniqueConstraint("user_id", "quest_id", name = "uq_user_quest"),)

  id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", name = 'fk_quest_progress_user_id'))
  quest_id: Mapped[int] = mapped_column(Integer, ForeignKey("quests.id"))
  status: Mapped[QuestStatus] = mapped_column(Enum(QuestStatus), server_default = QuestStatus.NOT_STARTED.value)
  started_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now())
  completed_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now(), onupdate = func.now())
  score: Mapped[int] = mapped_column(Integer, CheckConstraint("coins >= 0"), server_default = "0")

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
  reward_coins: Mapped[int] = mapped_column(Integer, CheckConstraint("coins >= 0"), server_default = "0")
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now(), onupdate = func.now())

  user_achievements: Mapped[List["UserAchievement"]] = relationship(
    back_populates = "achievement",
    cascade = "all, delete-orphan"
  )
class UserAchievement(Base):
  __tablename__ = "user_achievements"
  __table_args__ = (UniqueConstraint("user_id", "achievement_id", name = "uq_user_achievement"),)

  id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", name = 'fk_user_achievements_user_id'))
  achievement_id: Mapped[int] = mapped_column(Integer, ForeignKey("achievements.id"))
  achieved_at: Mapped[datetime] = mapped_column(DateTime, server_default = func.now(), onupdate = func.now())

  user: Mapped["User"] = relationship(
    back_populates = "achievements"
  )

  achievement: Mapped["Achievement"] = relationship(
    back_populates = "user_achievements"
  )