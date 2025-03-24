from database import SessionLocal
from models import User, UserProfile, Quests, QuestProgress, Achievement, UserAchievement

db = SessionLocal()

adilkhanix = db.query(User).filter_by(name = "adilkhanix").first()
kazmentor = db.query(User).filter_by(name = "kazmentor").first()
trump = db.query(User).filter_by(name = "trump").first()

quest1 = db.query(Quests).filter_by(id = 1).first()
quest2 = db.query(Quests).filter_by(id = 2).first()
quest3 = db.query(Quests).filter_by(id = 3).first()
quest4 = db.query(Quests).filter_by(id = 4).first()

achievement1 = db.query(Achievement).filter_by(id = 1).first()
achievement2 = db.query(Achievement).filter_by(id = 2).first()
achievement3 = db.query(Achievement).filter_by(id = 3).first()
achievement4 = db.query(Achievement).filter_by(id = 4).first()
achievement5 = db.query(Achievement).filter_by(id = 5).first()

try:
  user_lst = [
    User(
      name = "adilkhanix",
      email = "robbstarkst@gmail.com",
      password_hash = "$2y$10$BSZxgwv8lsWBJM.xJqlVOOVcfJBQGryo14FWp55qU.kWDiUqdOkrS"
    ),
    User(
      name = "kazmentor",
      email = "kazmentor@gmail.com",
      password_hash = "$2y$10$B8Iusk/v2tHfwrgN.t1MO.I7.7d9tubsG7zaC7gpjcYvRfWg03IBq"
    ),
    User(
      name = "trump",
      email = "trump@mail.ru",
      password_hash = "$2y$08$V6i.O6Oaue7PFa4ZMmXbCO0D1MqXn.4RdlEmKFix7luKkf22ZqiYu"
    )
  ]
  db.add_all(user_lst)
  db.commit()
except Exception as e:
  db.rollback()
  print(f"Error description: {e}")

try:
  user_profile_lst = [
    UserProfile(
      user_id = adilkhanix.id,
      display_name = "adilkhan",
      avatar_url = "/media/adilkhan.jpg",
      coins = 120,
      level = 5,
      experience = 35
    ),
    UserProfile(
      user_id = kazmentor.id,
      display_name = "kazakh",
      avatar_url = "/media/kazmentor.jpg",
      coins = 30,
      level = 2,
      experience = 12
    ),
    UserProfile(
      user_id = trump.id,
      display_name = "trump_master_69",
      avatar_url = "/media/trump.jpg",
      coins = 300,
      level = 7,
      experience = 69
    ),
  ]
  db.add_all(user_profile_lst)
  db.commit()
except Exception as e:
  db.rollback()
  print(f"Error description: {e}")


try:
  quests_lst = [
    Quests(
      title = "Basic Circuit Challenge",
      description = "Connect the wires to complete a simple electric circuit and light up the bulb.",
      difficulty = "EASY",
      reward_coins = 30
    ),
    Quests(
      title = "Electron Exploration",
      description = "Help the character discover the properties of an electron in the Electronium lab by solving physics problems.",
      difficulty = "MEDIUM",
      reward_coins = 70
    ),
    Quests(
      title = "Journey Through Forces",
      description = "Complete the quest by applying law of Newton and learn how forces work in the real world.",
      difficulty = "HARD",
      reward_coins = 120
    ),
    Quests(
      title = "Molecule Mystery",
      description = "Solve the puzzle using knowledge about molecular structures and chemical reactions.",
      difficulty = "MEDIUM",
      reward_coins = 90
    ),
  ]
  db.add_all(quests_lst)
  db.commit()
except Exception as e:
  db.rollback()
  print(f"Error description: {e}")


try:
  quest_progress_lst = [
    QuestProgress(
      user_id = kazmentor.id,
      quest_id = quest2.id,
      status = "IN_PROGRESS",
      score = 20
    ),
    QuestProgress(
      user_id = adilkhanix.id,
      quest_id = quest3.id,
      status = "COMPLETED",
      score = 50
    ),
    QuestProgress(
      user_id = trump.id,
      quest_id = quest4.id,
      status = "FAILED",
      score = 9
    ),
  ]
  db.add_all(quest_progress_lst)
  db.commit()
except Exception as e:
  db.rollback()
  print(f"Error description: {e}")

try:
  achievements_lst = [
    Achievement(
      name = "First Step",
      description = "Complete your first quest in KazMentor.",
      reward_coins = 10
    ),
    Achievement(
      name = "Physics Novice",
      description = "Solve 5 physics problems successfully.",
      reward_coins = 50
    ),
    Achievement(
      name = "Master of Forces",
      description = 'Complete the "Journey Through Forces" quest.',
      reward_coins = 100
    ),
    Achievement(
      name = "Molecule Detective",
      description = 'Unravel the "Molecule Mystery" without any hints.',
      reward_coins = 70
    ),
    Achievement(
      name = "Circuit Genius",
      description = "Build 3 electric circuits correctly in a row.",
      reward_coins = 80
    ),
  ]
  db.add_all(achievements_lst)
  db.commit()
except Exception as e:
  db.rollback()
  print(f"Error description: {e}")

try:
  users_achievements_lst = [
    UserAchievement(
      user_id = adilkhanix.id,
      achievement_id = achievement1.id
    ),
    UserAchievement(
      user_id = adilkhanix.id,
      achievement_id = achievement2.id
    ),
    UserAchievement(
      user_id = kazmentor.id,
      achievement_id = achievement1.id
    ),
    UserAchievement(
      user_id = kazmentor.id,
      achievement_id = achievement3.id
    ),
    UserAchievement(
      user_id = kazmentor.id,
      achievement_id = achievement4.id
    ),
    UserAchievement(
      user_id = trump.id,
      achievement_id = achievement1.id
    ),
    UserAchievement(
      user_id = trump.id,
      achievement_id = achievement5.id
    ),
  ]
  db.add_all(users_achievements_lst)
  db.commit()
except Exception as e:
  db.rollback()
  print(f"Error description: {e}")

finally:
  db.close()