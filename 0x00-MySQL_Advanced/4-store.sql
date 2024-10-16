-- add a trigger to decrease the quantity after an order
CREATE TRIGGER dec_quantity AFTER INSERT ON items
  FOR EACH ROW
  UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;