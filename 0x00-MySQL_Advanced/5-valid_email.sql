-- a trigger that after an update resets arre valid_email
-- only when the email has been changed
DELIMITER $$ 
CREATE TRIGGER validate_email 
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
IF OLD.email <> NEW.email 
THEN
  SET NEW.valid_email = 0;
END IF;
END
$$
DELIMITER;
