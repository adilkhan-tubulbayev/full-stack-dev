# KazMentor Database

This database is designed for the KazMentor educational platform with gamification elements. It manages users, their profiles, quests, quest progress, and achievements.

## Tables and Relationships

- **users**  
  Stores primary user data (username, email, password, role, and status).  
  _Relationship_: Serves as the main data source for other tables.

- **user_profiles**  
  Contains additional profile information (display name, avatar URL, coins, level, experience).  
  _Relationship_: References **users** (ON DELETE CASCADE).

- **quests**  
  Holds quest details (title, description, difficulty, reward coins).  
  _Relationship_: Used in **quest_progress**.

- **quest_progress**  
  Tracks users' progress on quests (status, start time, completion time, score).  
  _Relationship_: References **users** and **quests**.

- **achievements**  
  Contains achievement details (name, description, reward coins).

- **user_achievements**  
  Records which users have earned which achievements and when.  
  _Relationship_: References **users** and **achievements** (ON DELETE CASCADE).

## ENUM Types

- **role_enum**: `'student'`, `'teacher'`, `'admin'`
- **user_status_enum**: `'active'`, `'inactive'`
- **difficulty_enum**: `'easy'`, `'medium'`, `'hard'`
- **quest_status_enum**: `'not_started'`, `'in_progress'`, `'completed'`, `'failed'`

## Overview

- **Users & Profiles**: Handles registration, authentication, and extended user details.
- **Quests & Progress**: Manages quests and tracks user progress.
- **Achievements**: Awards users for reaching specific milestones.

This structure provides flexibility and scalability for efficiently managing the educational process and enhancing user engagement.
