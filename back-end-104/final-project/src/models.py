from sqlalchemy import (
		Column,
    Boolean,
    Date,
    DateTime,
    Float,
    Integer,
    String,
    Text,
    Time,
		Enum,
		enum,
		ForeignKey,
		text
)
from .database import Base

###ENUM CLASSES

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


###TABLES

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key = True, index = True)
	name = Column(String(100), nullable = False)
	email = Column(String(100), unique = True, nullable = False)
	password_hash = Column(String(255), nullable = False)
	role = Column(Enum(UserRole), server_default = UserRole.STUDENT)
	created_at = Column(DateTime, server_default = text('CURRENT_TIMESTAMP'))
	updated_at = Column(DateTime, server_default = text('CURRENT_TIMESTAMP') )
	status = Column(Enum(UserStatus), server_default = UserStatus.INACTIVE)


class UserProfile(Base):
	__tablename__ = "user_profiles"

	id = Column(Integer, primary_key = True, Index = True)
	user_id = Column(String(100), ForeignKey("users.id"))
	display_name = Column(String(50))
	avatar_url = Column(String(255))
	coins = Column(Integer, server_default = 0)
	level = Column(Integer, server_default = 1)
	experience = Column(Integer, server_default = 0)

class Quest(Base):
	__tablename__ = "quests"

	id = Column(Integer, primary_key = True, index = True)
	title = Column(String(255), nullable = False)
	description = Column(Text)
	difficulty = Column(Enum(LevelDifficulty), server_default = LevelDifficulty.EASY)
	reward_coins = Column(Integer, server_default = 0)
	created_at = Column(DateTime)
	updated_at = Column(DateTime)


class QuestProgress(Base):
	__tablename__ = "quest_progress"

	id = Column(Integer, primary_key = True, index = True)
	user_id = Column(Integer, ForeignKey("users.id"))
	quest_id = Column(Integer, ForeignKey("quests.id"))
	status = Column(Enum(QuestStatus), server_default = QuestStatus.NOT_STARTED)
	started_at = Column(DateTime)
	completed_at = Column(Date)
	score = Column(Integer, server_default = 0)


class Achievement(Base):
	__tablename__ = "achievements"
	
	id = Column(Integer, primary_key = True, index = True)
	name = Column(String(100), nullable = False)
	description = Column(Text)
	reward_coins = Column(Integer, server_default = 0)
	created_at = Column(DateTime)
	updated_at = Column(DateTime)


class UserAchievement(Base):
	__tablename__ = "user_achievements"

	id = Column(Integer, primary_key = True, index = True)
	user_id = Column(Integer, ForeignKey("users.id"))
	achievement_id = Column(Integer, ForeignKey("achievements.id"))
	achieved_at = Column(DateTime)

