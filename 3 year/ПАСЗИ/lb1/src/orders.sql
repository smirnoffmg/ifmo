CREATE TABLE IF NOT EXISTS `flowers`.`orders` (
  `id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `address` VARCHAR(255) NULL,
  `phone` VARCHAR(45) NULL,
  PRIMARY KEY (`id`, `user_id`),
  INDEX `fk_orders_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)