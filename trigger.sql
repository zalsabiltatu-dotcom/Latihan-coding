DELIMITER //

CREATE TRIGGER inkremenStok2
BEFORE INSERT ON barang
FOR EACH ROW BEGIN

    -- Menambah nilai stok dengan 1
    SET NEW.stok = NEW.stok + 1;

END //

DELIMITER ;