-- a stored procedure AddBonus that 
-- adds a new correction for a student
DELIMITER ##
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255),  IN score FLOAT)
BEGIN
  DECLARE pr_id INT;

  SELECT id INTO pr_id 
  FROM projects
  WHERE name = project_name;

  IF pr_id IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name);
    SELECT LAST_INSERT_ID() INTO pr_id;
  END IF;
  INSERT INTO corrections VALUES (user_id, pr_id, score);
END
##
DELIMITER;
