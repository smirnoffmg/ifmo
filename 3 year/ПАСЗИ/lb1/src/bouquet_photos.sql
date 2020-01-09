CREATE TABLE IF NOT EXISTS `flowers`.`bouquet_photos` (
  `id` INT NOT NULL,
  `photo` VARCHAR(45) NULL,
  `bouquets_id` INT NOT NULL,
  PRIMARY KEY (`id`, `bouquets_id`),
  INDEX `fk_bouquet_photos_bouquets1_idx` (`bouquets_id` ASC) VISIBLE,
  CONSTRAINT `fk_bouquet_photos_bouquets1`
    FOREIGN KEY (`bouquets_id`)
    REFERENCES `mydb`.`bouquets` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)