-- add a trigger to decrease the quantity after an order
delimiter |
CREATE TRIGGER dec_quantity AFTER INSERT ON items
  FOR EACH ROW
  BEGIN
    UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name
  End;
delimiter;