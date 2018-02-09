<?php
echo "Hello! World!<br>";
echo $_ENV['MYSQL_HOST'];
echo "<br>";
echo $_ENV['MYSQL_USER'];
echo "<br>";
echo $_ENV['MYSQL_PASSWORD'];
echo "<br>";
echo $_ENV['MYSQL_DATABASE'];
echo "<br>";
$mysql = new mysqli($_ENV['MYSQL_HOST'], $_ENV['MYSQL_USER'],
	$_ENV['MYSQL_PASSWORD'], $_ENV['MYSQL_DATABASE']);
if (!$mysql) {
	echo "Error: Unable to connect to MySQL." . PHP_EOL;
	echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
	exit;
}
$sql = "INSERT INTO score(created_at) VALUES('" . date('Y-m-d H:i:s') . "')";
$result = $mysql->query($sql);
$sql = "SELECT * FROM score ORDER BY id desc limit 1";
$result = $mysql->query($sql)->fetch_row();
var_dump($result);
mysqli_close($mysql);
phpinfo();
