--- EXAMPLES OF QUERIES --

-- JOIN --
SELECT *
FROM users
FULL JOIN quest_progress ON users.id = quest_progress.user_id;

SELECT *
FROM users
lEFT JOIN user_achievements ON users.id = user_achievements.user_id;

SELECT users.username, users.email, quest_progress.status, quest_progress.started_at, quest_progress.completed_at, quest_progress.score
FROM quest_progress
RIGHT JOIN users ON quest_progress.user_id = users.id
WHERE score > ( -- SUBQUERY
  SELECT AVG(score)
  FROM quest_progress
);

SELECT *
FROM users
WHERE id > 1; -- WHERE FOR FILTRATION

SELECT *
FROM quest_progress;

SELECT *
FROM user_profiles
ORDER BY coins DESC; -- ORDER BY

CREATE VIEW users_coins AS --VIEW
SELECT *
FROM user_profiles
WHERE experience > 100 OR coins > 40;

SELECT *
FROM users_coins;

UPDATE users -- UPDATE
SET username = 'trump_maga'
WHERE id = 3;

DELETE FROM user_profiles WHERE id = 2; -- DELETE

SELECT *
FROM user_profiles
WHERE id = 2;


CREATE OR REPLACE FUNCTION calculate_additional_coins( -- SIMPLE FUNCTION
  level INTEGER
)
RETURNS INTEGER AS $$
BEGIN
  RETURN CASE
    WHEN level > 2 THEN 10
    WHEN level > 5 THEN 20
    WHEN level > 10 THEN 30
    ELSE 5
  END;
END;
$$ LANGUAGE plpgsql;


SELECT -- TESTING OF FUNCTION
  display_name,
  coins,
  level,
  calculate_additional_coins(level) AS extra_coins
FROM user_profiles;
