-- computes and store the average score for a student

DELIMITER ##
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE avg FLOAT;
  SELECT AVG(score) INTO avg FROM corrections as X WHERE X.user_id = user_id;
  UPDATE users SET average_score = avg WHERE user_id = id;
END
##
DELIMITER;
  