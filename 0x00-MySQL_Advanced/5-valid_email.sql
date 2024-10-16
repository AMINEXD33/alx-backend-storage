-- a trigger that after an update checks if the email is valid or not

CREATE TRIGGER  validate_email 
AFTER UPDATE
FOR EACH ROW
BEGIN
IF OLD.email <> NEW.email THEN
  SET NEW.valid_email = 0
END IF;
END
