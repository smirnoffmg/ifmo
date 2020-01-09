CREATE TABLE IF NOT EXISTS `flowers`.`order_items` (
  `id` INT NOT NULL,
  `price` FLOAT NOT NULL,
  `bouquets_id` INT NOT NULL,
  `orders_id` INT NOT NULL,
  `orders_user_id` INT NOT NULL,
  PRIMARY KEY (`id`, `bouquets_id`, `orders_id`, `orders_user_id`),
  INDEX `fk_order_items_bouquets1_idx` (`bouquets_id` ASC) VISIBLE,
  INDEX `fk_order_items_orders1_idx` (`orders_id` ASC, `orders_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_items_bouquets1`
    FOREIGN KEY (`bouquets_id`)
    REFERENCES `mydb`.`bouquets` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_items_orders1`
    FOREIGN KEY (`orders_id` , `orders_user_id`)
    REFERENCES `mydb`.`orders` (`id` , `user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)