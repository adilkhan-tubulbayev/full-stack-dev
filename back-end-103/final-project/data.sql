-- INITIAL DATA INSERTION --

INSERT INTO users(username, email, password_hash) VALUES 
('adilkhanix', 'robbstarkst@gmail.com', '$2y$10$BSZxgwv8lsWBJM.xJqlVOOVcfJBQGryo14FWp55qU.kWDiUqdOkrS'),
('kazmentor', 'kazmentor@gmail.com', '$2y$10$B8Iusk/v2tHfwrgN.t1MO.I7.7d9tubsG7zaC7gpjcYvRfWg03IBq'),
('trump', 'trump@mail.ru', '$2y$08$V6i.O6Oaue7PFa4ZMmXbCO0D1MqXn.4RdlEmKFix7luKkf22ZqiYu');

INSERT INTO user_profiles(user_id, display_name, avatar_url, coins, level, experience) VALUES
(1, 'adilkhan', '/media/adilkhan.jpg', 120, 5, 35),
(2, 'kazakh', '/media/kazmentor.jpg', 30, 2, 12),
(3, 'trump_master_69', '/media/trump.jpg', 300, 7, 69);

INSERT INTO quests(title, description, difficulty, reward_coins) VALUES
('Basic Circuit Challenge', 'Connect the wires to complete a simple electric circuit and light up the bulb.', 'easy', 30),
('Electron Exploration', 'Help the character discover the properties of an electron in the Electronium lab by solving physics problems.', 'medium', 70),
('Journey Through Forces', 'Complete the quest by applying law of Newton and learn how forces work in the real world.', 'hard', 120),
('Molecule Mystery', 'Solve the puzzle using knowledge about molecular structures and chemical reactions.', 'medium', 90);

INSERT INTO quest_progress(user_id, quest_id, status, started_at, score) VALUES
(2, 2, 'in_progress', '2024-02-24 14:30:00', 20),
(1, 3, 'completed', '2024-05-12 12:46:32', 50),
(3, 4, 'failed', '2024-08-05 21:52:19', 9);

INSERT INTO achievements(name, description, reward_coins) VALUES
('First Step', 'Complete your first quest in KazMentor.', 10),
('Physics Novice', 'Solve 5 physics problems successfully.', 50),
('Master of Forces', 'Complete the "Journey Through Forces" quest.', 100),
('Molecule Detective', 'Unravel the "Molecule Mystery" without any hints.', 70),
('Circuit Genius', 'Build 3 electric circuits correctly in a row.', 80);

INSERT INTO user_achievements(user_id, achievement_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(2, 4),
(3, 1),
(3, 5);
