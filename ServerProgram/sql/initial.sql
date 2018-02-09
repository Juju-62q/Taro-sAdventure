CREATE TABLE 'SCORE'{
  'id' int(20) unsigned NOT NULL AUTO_INCREMENT,
  'name' varchar(20),
  'score' int(20) unsigned,
  'created_time' datetime NOT NULL,
  PRIMARY KEY ('id')
} ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
