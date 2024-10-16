-- a trigger that after an update checks if the email is valid or not
CREATE TRIGGER  validate_email 
AFTER UPDATE
FOR EACH ROW
IF OLD.email = NEW.email THEN
  NEW.valid_email = 0
ELSE
  NEW.valid_email = 1
END IF;
