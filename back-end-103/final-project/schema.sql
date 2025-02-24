-- TABLES --

CREATE TYPE role_enum AS ENUM('student', 'teacher', 'admin');
CREATE TYPE user_status_enum AS ENUM('active', 'inactive');
CREATE TYPE difficulty_enum AS ENUM('easy', 'medium', 'hard');
CREATE TYPE quest_status_enum AS ENUM('not_started', 'in_progress', 'completed', 'failed');


CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ROLE_ENUM DEFAULT 'student',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status USER_STATUS_ENUM DEFAULT 'inactive'
);

CREATE TABLE user_profiles(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES users(id)  ON DELETE CASCADE,
  display_name VARCHAR(50),
  avatar_url VARCHAR(255),
  coins INTEGER DEFAULT 0,
  level INTEGER DEFAULT 1,
  experience INTEGER DEFAULT 0
);

CREATE TABLE quests(
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  difficulty DIFFICULTY_ENUM DEFAULT 'easy',
  reward_coins INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP
);

CREATE TABLE quest_progress(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
  quest_id INTEGER,
  FOREIGN KEY(quest_id) REFERENCES quests(id),
  status QUEST_STATUS_ENUM DEFAULT 'not_started',
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  score INTEGER DEFAULT 0
);

CREATE TABLE achievements(
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  reward_coins INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP
);

CREATE TABLE user_achievements(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
  achievement_id INTEGER,
  FOREIGN KEY(achievement_id) REFERENCES achievements(id) ON DELETE CASCADE,
  achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

